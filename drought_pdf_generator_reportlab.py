# Import libraries
import pandas as pd
from pandasql import sqldf
# from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.platypus.tables import Table,TableStyle,colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

# def get_data_vahydro(viewurl, baseurl = "http://deq1.bse.vt.edu:81/d.dh"):
def get_data_vahydro(viewurl, baseurl = "https://deq1.bse.vt.edu/d.dh"):
    url = baseurl + "/" + viewurl
    # print("Retrieving Data From: " + url)
    df=pd.read_csv(url)
    return df

def add_rownum_to_nested_list(data_list):
    data_list_WithRowNums = []
    for i in range(len(data_list)):
        data_list_unnested = data_list[i]
        data_list_unnested.insert(0, i+1)
        data_list_WithRowNums.append(data_list_unnested)
    return(data_list_WithRowNums)


precip_df = get_data_vahydro(viewurl = 'precipitation-drought-timeseries-export')
precip_df = sqldf("""SELECT `drought_region` AS region, 
                            `startdate` AS startdate, 
                            `enddate` AS enddate,
                            `[Water_Year_pct_of_Normal]_propvalue` AS 'water yr % of normal',
                            CASE
                                WHEN `[Drought_Status]_propcode` = 1 THEN 'Watch'
                                WHEN `[Drought_Status]_propcode` = 2 THEN 'Warning'
                                WHEN `[Drought_Status]_propcode` = 3 THEN 'Emergency'
                            END AS status
                        FROM precip_df
                        WHERE `[Drought_Status]_propcode` > 0
                        ORDER BY status DESC""")
# print(f'Precipitation Indicators:\n{precip_df}\n')
precip_pd = pd.DataFrame(precip_df)

sw_df = get_data_vahydro(viewurl = 'streamflow-drought-timeseries-all-export')

# reutrn only the 11 official drought evaluation region stream gage indicators
sw_official_df = sw_df[pd.notna(sw_df)['drought_evaluation_region'] == True]

# sqldf method below:
# note: 3-quote method allows formatting query across multiple lines
# sw_status_df = sqldf("""SELECT `drought_evaluation_region` AS region, 
#                             `[q_7day_cfs]_tstime` AS tstime, 
#                             `[q_7day_cfs]_tsendtime` AS tsendtime, 
#                             `[nonex_pct]_propvalue` AS 'percentile',
#                             `[nonex_pct]_propcode` AS status, 
#                             `drought_status_override` AS override,
#                             CASE
#                                 WHEN `drought_status_override` < `[nonex_pct]_propcode` THEN `drought_status_override`
#                                 ELSE `[nonex_pct]_propcode`
#                             END AS final_status
#                         FROM sw_official_df
#                         WHERE `[nonex_pct]_propcode` > 0""")

sw_status_df = sqldf("""SELECT `drought_evaluation_region` AS region, 
                            `[q_7day_cfs]_tstime` AS tstime, 
                            `[q_7day_cfs]_tsendtime` AS tsendtime, 
                            `[nonex_pct]_propvalue` AS 'percentile',
                            CASE
                                WHEN `[nonex_pct]_propcode` = 1 THEN 'Watch'
                                WHEN `[nonex_pct]_propcode` = 2 THEN 'Warning'
                                WHEN `[nonex_pct]_propcode` = 3 THEN 'Emergency'
                            END AS status
                        FROM sw_official_df
                        WHERE `[nonex_pct]_propcode` > 0
                        ORDER BY status DESC""")
                        # FROM sw_official_df""") 
# print(f'Surface Water Indicators:\n{sw_status_df}\n')
sw_pd = pd.DataFrame(sw_status_df)

# format table using CTE temporary table
sw_status_df_all = sqldf("""WITH cte AS(
                                SELECT  CASE
                                        WHEN `drought_status_override` < `[nonex_pct]_propcode` THEN `drought_status_override`
                                            ELSE `[nonex_pct]_propcode`
                                        END AS final_status,
                                        COUNT(`containing_drought_region`) AS gage_count
                                FROM sw_df
                                WHERE `[nonex_pct]_propcode` > 0
                                GROUP BY final_status 
                            )

                            SELECT  CASE
                                        WHEN `final_status` = 1 THEN 'watch'
                                        WHEN `final_status` = 2 THEN 'warning'
                                        WHEN `final_status` = 3 THEN 'emergency'
                                    END AS gage_status,
                                    gage_count
                            FROM cte
                            """)

# print(f'Surface Water Indicators (All):\n{sw_status_df_all}\n')
sw_all_pd = pd.DataFrame(sw_status_df_all)

gw_df = get_data_vahydro(viewurl = 'groundwater-drought-timeseries-all-export')

# return only those with a below normal drought status
# retuen the maximum status by region for those regions with multiple gw indicators
# gw_max_status_df = sqldf("""SELECT `drought_evaluation_region` AS region, 
#                                 `[gwl_7day_ft]_tstime` AS tstime, 
#                                 `[gwl_7day_ft]_tsendtime` AS tsendtime,
#                                 `[nonex_pct]_propvalue` AS 'percentile', 
#                                 MAX(`[nonex_pct]_propcode`) AS max_status, 
#                                 `drought_status_override` AS override,
#                                 CASE
#                                     WHEN `drought_status_override` < `[nonex_pct]_propcode` THEN `drought_status_override`
#                                     ELSE `[nonex_pct]_propcode`
#                                 END AS final_status
#                             FROM gw_df
#                             WHERE `[nonex_pct]_propcode` > 0
#                             GROUP BY `drought_evaluation_region`""")
gw_max_status_df = sqldf("""SELECT `drought_evaluation_region` AS region, 
                                `[gwl_7day_ft]_tstime` AS tstime, 
                                `[gwl_7day_ft]_tsendtime` AS tsendtime,
                                `[nonex_pct]_propvalue` AS 'percentile', 
                                CASE
                                    WHEN MAX(`[nonex_pct]_propcode`) = 1 THEN 'Watch'
                                    WHEN MAX(`[nonex_pct]_propcode`) = 2 THEN 'Warning'
                                    WHEN MAX(`[nonex_pct]_propcode`) = 3 THEN 'Emergency'
                                END AS max_status
                            FROM gw_df
                            WHERE `[nonex_pct]_propcode` > 0
                            GROUP BY `drought_evaluation_region`
                            ORDER BY MAX(`[nonex_pct]_propcode`) DESC""")
# print(f'Groundwater Indicators:\n{gw_max_status_df}\n')
gw_pd = pd.DataFrame(gw_max_status_df)


res_df = get_data_vahydro(viewurl = 'reservoir-drought-features-export')
# print(res_df.head())
res_status_df = sqldf("""SELECT `Drought Region`, `Feature Name`, `Drought Status (propcode)` 
                        FROM res_df 
                        """)

###############################################################
###############################################################
today = date.today()
today = today.strftime('%m/%d/%Y')
print("Today's date:", today)

# my_path='C:\\Users\\jklei\\Desktop\\Learning Python\\pydro-tools\\reportlab_test2.pdf'
# my_path='C:\\Users\\nrf46657\\Desktop\\GitHub\\pydro-tools\\reportlab_test.pdf'
output_filename = "C:\\Users\\nrf46657\\Desktop\\GitHub\\pydro-tools\\" + "Daily_Drought_Indicator_Status_{}.pdf".format(date.today().strftime('%m.%d.%Y'))
my_doc = SimpleDocTemplate(output_filename,pagesize=letter)
styles = getSampleStyleSheet()

c_width=[0.4*inch,2.0*inch,1*inch,1*inch,1*inch,0.7*inch,0.7*inch] # width of the columns 

precip_data=precip_pd.values.tolist() # create a list using Dataframe
precip_data=add_rownum_to_nested_list(precip_data)
# precip_colnames = [['#', 'region', 'startdate', 'enddate', 'water yr %\nof normal', 'status','','']]
precip_colnames = [['#', 'Region', 'Start Date', 'End Date', 'Water Year\n% of Normal', 'Status']]
precip_data = precip_colnames + precip_data
precip_t=Table(precip_data,colWidths=c_width,repeatRows=1)
precip_t.setStyle(TableStyle([('FONTSIZE',(0,0),(-1,-1),12),('BACKGROUND',(0,0),(-1,0),colors.lightgrey),('VALIGN',(0,0),(-1,0),'TOP')]))

sw_data=sw_pd.values.tolist() # create a list using Dataframe
sw_data=add_rownum_to_nested_list(sw_data)
# colnames = [['#','region', 'tstime', 'tsendtime', 'percentile', 'status', 'override', 'final_status']]
colnames = [['#','Region', 'Start Date', 'End Date', 'Percentile', 'Status']]
sw_data = colnames + sw_data
sw_t=Table(sw_data,colWidths=c_width,repeatRows=1)
sw_t.setStyle(TableStyle([('FONTSIZE',(0,0),(-1,-1),12),('BACKGROUND',(0,0),(-1,0),colors.lightgrey),('VALIGN',(0,0),(-1,0),'TOP')]))

gw_data=gw_pd.values.tolist() # create a list using Dataframe
gw_data=add_rownum_to_nested_list(gw_data)
gw_data = colnames + gw_data
gw_t=Table(gw_data,colWidths=c_width,repeatRows=1)
gw_t.setStyle(TableStyle([('FONTSIZE',(0,0),(-1,-1),12),('BACKGROUND',(0,0),(-1,0),colors.lightgrey),('VALIGN',(0,0),(-1,0),'TOP')]))

elements=[]
title = "DEQ Daily Drought Indicator Status: {}".format(today)
elements.append(Paragraph(title, styles['Title']))

img_file = "https://deq1.bse.vt.edu/drought/state/images/maps/virginia_drought.png"
# map_img = Image(img_file, 3*inch, 3*inch)
map_img = Image(img_file, 5*inch, 3*inch)
elements.append(map_img)

elements.append(Spacer(1,0.2*inch))
precip_text = Paragraph("Precipitation Indicators:", styles['Heading3'])
elements.append(precip_text)
elements.append(precip_t)

elements.append(Spacer(1,0.2*inch))
sw_text = Paragraph("Surface Water Indicators:", styles['Heading3'])
elements.append(sw_text)
elements.append(sw_t)

elements.append(Spacer(1,0.2*inch))
gw_text = Paragraph("Groundwater Indicators:", styles['Heading3'])
elements.append(gw_text)
elements.append(gw_t)

my_doc.build(elements)
###############################################################