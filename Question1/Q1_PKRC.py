 
import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 

def q1_pkrc():  
    pkrc = pd.read_csv('Dataset/pkrc.csv')

    pkrc['date']= pd.to_datetime(pkrc['date'])
    pkrc.rename(columns= {
        "admitted_pui": "pkrc_admitted_pui",
        "admitted_covid": "pkrc_admitted_covid",
        "admitted_total": "pkrc_admitted_total",
        "discharge_pui": "pkrc_discharged_pui",
        "discharge_covid": "pkrc_discharged_covid",
        "discharge_total": "pkrc_discharged_total"
    }, inplace=True)

    state_pkrc = pkrc.groupby(['state']).sum()

    month = {'2020-03-31 00:00:00':'March', '2020-04-30 00:00:00':'April','2020-05-31 00:00:00':'May','2020-06-30 00:00:00':'June','2020-07-31 00:00:00':'July','2020-08-31 00:00:00':'August','2020-09-30 00:00:00':'September','2020-10-31 00:00:00':'October','2020-11-30 00:00:00':'November','2020-12-31 00:00:00':'December',
            '2021-01-31 00:00:00':'January','2021-02-28 00:00:00':'February','2021-03-31 00:00:00':'March','2021-04-30 00:00:00':'April','2021-05-31 00:00:00':'May','2021-06-30 00:00:00':'June','2021-07-31 00:00:00':'July','2021-08-31 00:00:00':'August','2021-09-30 00:00:00':'September',}
    month_pkrc = pkrc.groupby([pd.Grouper(key='date', axis=0, freq='M'),"state"]).agg('sum')
    m_pkrc = pkrc.groupby(pd.Grouper(key='date', axis=0, freq='M')).sum()
    maxMonth1 = str(m_pkrc['pkrc_admitted_covid'].idxmax())
    maxMonth2 = str(m_pkrc['pkrc_discharged_covid'].idxmax())

    selectShow = st.selectbox("Select an aspect to show", ['Outliers Detection','Data Analysis'])

    if selectShow == 'Outliers Detection': 
        c1,c2= st.columns(2)
        with c1:
            boxplot1 = alt.Chart(pkrc).mark_boxplot().encode(
                y='beds:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total PKRC Beds'
                    )

            st.altair_chart(boxplot1)

        with c2:
            boxplot2 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_admitted_pui:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Number of Individuals(PUI) Admitted to PKRC'
                    )

            st.altair_chart(boxplot2)
        
        c3,c4= st.columns(2)
        with c3:
            boxplot3 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_admitted_covid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Number of COVID-19 Patients Admitted to PKRC'
                    )

            st.altair_chart(boxplot3)

        with c4:
            boxplot4 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_admitted_total:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of Patients Admitted to PKRC'
                    )

            st.altair_chart(boxplot4)
        
        c5,c6= st.columns(2)
        with c5:
            boxplot5 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_discharged_pui:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Number of individuals(PUI) discharged from PKRC'
                    )

            st.altair_chart(boxplot5)

        with c6:
            boxplot6 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_discharged_covid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Number of COVID-19 Patients discharged from PKRC'
                    )

            st.altair_chart(boxplot6)
        
        c7,c8= st.columns(2)
        with c7:
            boxplot7 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_discharged_total:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of Patients discharged from PKRC'
                    )

            st.altair_chart(boxplot7)

        with c8:
            boxplot8 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_covid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of COVID-19 Patients in PKRC'
                    )

            st.altair_chart(boxplot8)
        
        c9,c10= st.columns(2)
        with c9:
            boxplot9 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_pui:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of Individuals(PUI) in PKRC'
                    )

            st.altair_chart(boxplot9)

        with c10:
            boxplot10 = alt.Chart(pkrc).mark_boxplot().encode(
                y='pkrc_noncovid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of Non-COVID-19 Patients in PKRC'
                    )

            st.altair_chart(boxplot10)
        st.markdown('Based on the boxplot above, we can see that every column in the pkrc.csv dataset contains a lot of outliers. All of the boxplots showed that the data is positively skewed. This may be due to the slow start of the COVID-19 pandemic which contains a low number of COVID-19 cases, followed by a sudden increase of high number COVID-19 cases that caused a high number of patients admitted to the PKRC. However, we decided to not remove these outliers as the data are crucial to this assignment and training model.')
        
    else:
        left_column2, right_column2 = st.columns(2)
        with left_column2:
            selectGroupBy = st.selectbox("View By", ['Day','Month'])

        with right_column2:
            selectState = st.selectbox("Select a state to view", ['All','Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'])

        if selectGroupBy == 'Day':
            if selectState == 'All':
                dayAllAChart = alt.Chart(pkrc).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('pkrc_admitted_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Admission of COVID-19 Patient in PKRC by Day'
                )
               
                id = pkrc['pkrc_admitted_covid'].idxmax()
                day = pkrc.loc[id].date
                state = pkrc.loc[id].state
                st.altair_chart(dayAllAChart)
                st.markdown("The total COVID-19 patient admission in PKRC of Malaysia is " + str(state_pkrc['pkrc_admitted_covid'].sum()))
                st.markdown("The mean COVID-19 patient admission in PKRC of Malaysia is " + str(state_pkrc['pkrc_admitted_covid'].mean()))
                st.markdown("The state with the most COVID-19 patient admission in PKRC is " + str(state_pkrc['pkrc_admitted_covid'].idxmax()) + ' at ' + str(state_pkrc['pkrc_admitted_covid'].max()))
                st.markdown("The day with the most COVID-19 patient admission in PKRC is " + str(day) + ' in ' + state +' at ' + str(pkrc['pkrc_admitted_covid'].max()))

                dayAllDChart = alt.Chart(pkrc).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('pkrc_discharged_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Discharge of COVID-19 Patient in PKRC by Day'
                )
               
                id_dAll = pkrc['pkrc_discharged_covid'].idxmax()
                day_dAll = pkrc.loc[id_dAll].date
                state_dAll = pkrc.loc[id_dAll].state
                st.altair_chart(dayAllDChart)
                st.markdown("The total discharge of COVID-19 patients in PKRC of Malaysia is " + str(state_pkrc['pkrc_discharged_covid'].sum()))
                st.markdown("The mean discharge of COVID-19 patients in PKRC of Malaysia is " + str(state_pkrc['pkrc_discharged_covid'].mean()))
                st.markdown("The state with the most discharge of COVID-19 patient in PKRC is " + str(state_pkrc['pkrc_discharged_covid'].idxmax()) + ' at ' + str(state_pkrc['pkrc_discharged_covid'].max()))
                st.markdown("The day with the most discharge of COVID-19 patient in PKRC is " + str(day_dAll) + ' in ' + state_dAll +' at ' + str(pkrc['pkrc_discharged_covid'].max()))
                st.markdown("The line graph above has shown that Selangor recorded the highest number of admission and discharge of COVID-19 patients in the PKRC for every month. This has proven that Selangor is the most severe state in Malaysia. However, based on the graphs above, it can be seen that total discharges of COVID-19 patients in PKRC are almost the same as the total admission of COVID-19 patients in PKRC for every month. This can be proven that the recovery rate of COVID-19 patients who undergo quarantine at PKRC is high and death rate is low.")
                st.markdown("Besides, it can be noticed that there are two peaks in both of the graphs. It can be deduced that the total number of COVID-19 cases for every month was low at the early stages and the COVID-19 cases increased significantly from December 2020 to March 2021. After that, the cases dropped significantly and a second wave started in June 2021.")
            else:
                state_day_total1 = pkrc[pkrc['state'] == selectState]
                state_day_chart1 = alt.Chart(state_day_total1).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('pkrc_admitted_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Admission of COVID-19 Patient in PKRC for ' + selectState + ' by Day'
                )
                day_ad_all = state_day_total1['pkrc_admitted_covid'].idxmax()
                day_ad_all = state_day_total1.loc[day_ad_all].date

                st.altair_chart(state_day_chart1)
                st.markdown("The total admission of COVID-19 Patient in PKRC for " + selectState + ' is ' + str(state_day_total1['pkrc_admitted_covid'].sum()))        
                st.markdown("The mean death  Admission of COVID-19 Patient in PKRC for " + selectState + ' is ' + str(state_day_total1['pkrc_admitted_covid'].mean()))     
                st.markdown("The day with the most admission of COVID-19 Patient in PKRC for " + str(day_ad_all) + ' at ' + str(state_day_total1['pkrc_admitted_covid'].max()))    
        
                state_day_total2 = pkrc[pkrc['state'] == selectState]
                state_day_chart2 = alt.Chart(state_day_total2).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('pkrc_discharged_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Discharged of COVID-19 Patient in PKRC for ' + selectState + ' by Day'
                )
                day_dc_all = state_day_total1['pkrc_discharged_covid'].idxmax()
                day_dc_all = state_day_total1.loc[day_dc_all].date

                st.altair_chart(state_day_chart2)
                st.markdown("The total discharge of COVID-19 Patient in PKRC for " + selectState + ' is ' + str(state_day_total2['pkrc_discharged_covid'].sum()))        
                st.markdown("The mean discharge of COVID-19 Patient in PKRC for " + selectState + ' is ' + str(state_day_total2['pkrc_discharged_covid'].mean()))     
                st.markdown("The day with the most discharge of COVID-19 Patient is " + str(day_dc_all) + ' at ' + str(state_day_total2['pkrc_discharged_covid'].max()))
                st.markdown("The line graph above has shown that Selangor recorded the highest number of admission and discharge of COVID-19 patients in the PKRC for every month. This has proven that Selangor is the most severe state in Malaysia. However, based on the graphs above, it can be seen that total discharges of COVID-19 patients in PKRC are almost the same as the total admission of COVID-19 patients in PKRC for every month. This can be proven that the recovery rate of COVID-19 patients who undergo quarantine at PKRC is high and death rate is low.")
                st.markdown("Besides, it can be noticed that there are two peaks in both of the graphs. It can be deduced that the total number of COVID-19 cases for every month was low at the early stages and the COVID-19 cases increased significantly from December 2020 to March 2021. After that, the cases dropped significantly and a second wave started in June 2021.")
        else:
            if selectState == 'All':
                month_pkrc = month_pkrc.reset_index()
                monthChart1 = alt.Chart(month_pkrc).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('pkrc_admitted_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Admission of COVID-19 Patient in PKRC for every Month'
                )
                
                st.altair_chart(monthChart1)
                st.markdown("The total COVID-19 patient admission in PKRC of Malaysia is " + str(state_pkrc['pkrc_admitted_covid'].sum()))
                st.markdown("The mean COVID-19 patient admission in PKRC of Malaysia is " + str(state_pkrc['pkrc_admitted_covid'].mean()))
                st.markdown("The state with the most COVID-19 patient admission in PKRC is " + str(state_pkrc['pkrc_admitted_covid'].idxmax()) + ' at ' + str(state_pkrc['pkrc_admitted_covid'].max()))
                st.markdown("The month with the most COVID-19 patient admission in PKRC(from 2020-2021) is " +  month[maxMonth1] + ' at ' + str(m_pkrc['pkrc_admitted_covid'].max()))

                monthChart2 = alt.Chart(month_pkrc).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('pkrc_discharged_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Discharge of COVID-19 Patient in PKRC for every Month'
                )
                
                st.altair_chart(monthChart2)
                st.markdown("The total discharge of COVID-19 patient in PKRC of Malaysia is " + str(state_pkrc['pkrc_discharged_covid'].sum()))
                st.markdown("The mean discharge of COVID-19 patient in PKRC of Malaysia is " + str(state_pkrc['pkrc_discharged_covid'].mean()))
                st.markdown("The state with the most discharge of COVID-19 patient in PKRC is " + str(state_pkrc['pkrc_discharged_covid'].idxmax()) + ' at ' + str(state_pkrc['pkrc_admitted_covid'].max()))
                st.markdown("The month with the most discharge of COVID-19 patient in PKRC(from 2020-2021) is " +  month[maxMonth2] + ' at ' + str(m_pkrc['pkrc_discharged_covid'].max()))
                st.markdown("The line graph above has shown that Selangor recorded the highest number of admission and discharge of COVID-19 patients in the PKRC for every month. This has proven that Selangor is the most severe state in Malaysia. However, based on the graphs above, it can be seen that total discharges of COVID-19 patients in PKRC are almost the same as the total admission of COVID-19 patients in PKRC for every month. This can be proven that the recovery rate of COVID-19 patients who undergo quarantine at PKRC is high and death rate is low.")
                st.markdown("Besides, it can be noticed that there are two peaks in both of the graphs. It can be deduced that the total number of COVID-19 cases for every month was low at the early stages and the COVID-19 cases increased significantly from December 2020 to March 2021. After that, the cases dropped significantly and a second wave started in June 2021.")
            else:
                month_pkrc = month_pkrc.reset_index()
                state_month_total1 = month_pkrc[month_pkrc['state'] == selectState]
                stateMonthChart1 = alt.Chart(state_month_total1).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('pkrc_admitted_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Admission of COVID-19 Patient in PKRC for' + selectState + ' by Month'            
                )
                st.altair_chart(stateMonthChart1)
                st.markdown("The total admission of COVID-19 patient in PKRC for " + selectState + ' is ' + str(state_month_total1['pkrc_admitted_covid'].sum()))        
                st.markdown("The mean admission of COVID-19 patient in PKRC for " + selectState + ' is ' + str(state_month_total1['pkrc_admitted_covid'].mean()))     
                st.markdown("The highest number of admission of COVID-19 patients in PKRC  for " + selectState + ' is ' + str(state_month_total1['pkrc_admitted_covid'].max()))

                state_month_total2 = month_pkrc[month_pkrc['state'] == selectState]
                stateMonthChart2 = alt.Chart(state_month_total2).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('pkrc_discharged_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total discharge of COVID-19 Patient in PKRC for' + selectState + ' by Month'            
                )
                st.altair_chart(stateMonthChart2)
                st.markdown("The total discharge of COVID-19 patient in PKRC for " + selectState + ' is ' + str(state_month_total2['pkrc_discharged_covid'].sum()))        
                st.markdown("The mean discharge of COVID-19 patient in PKRC for " + selectState + ' is ' + str(state_month_total2['pkrc_discharged_covid'].mean()))     
                st.markdown("The highest number of discharge of COVID-19 patients in PKRC  for " + selectState + ' is ' + str(state_month_total2['pkrc_discharged_covid'].max()))
                st.markdown("The line graph above has shown that Selangor recorded the highest number of admission and discharge of COVID-19 patients in the PKRC for every month. This has proven that Selangor is the most severe state in Malaysia. However, based on the graphs above, it can be seen that total discharges of COVID-19 patients in PKRC are almost the same as the total admission of COVID-19 patients in PKRC for every month. This can be proven that the recovery rate of COVID-19 patients who undergo quarantine at PKRC is high and death rate is low.")
                st.markdown("Besides, it can be noticed that there are two peaks in both of the graphs. It can be deduced that the total number of COVID-19 cases for every month was low at the early stages and the COVID-19 cases increased significantly from December 2020 to March 2021. After that, the cases dropped significantly and a second wave started in June 2021.")