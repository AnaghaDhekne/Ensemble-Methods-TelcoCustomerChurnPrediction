from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import Churn_Prediction_Utils
import Global_Defs


def getDemographicStats(df):
    colors = Global_Defs.getColors()
    categorical_columns = Churn_Prediction_Utils.getCategoricalColumns(df)
    figure1 = make_subplots(rows=2, cols=2, subplot_titles=['Gender Distribution', 'Senior Citizen Distribution', 'Partner Status', 'Dependents Status'])
    figure1.add_trace(go.Bar(x=categorical_columns['Gender'].value_counts().index, y=categorical_columns['Gender'].value_counts(), text=(categorical_columns['Gender'].value_counts()*100/categorical_columns['Gender'].shape[0]).round(2), width=[0.5, 0.5], marker={'color':colors[0]}), row=1, col=1)
    figure1.add_trace(go.Bar(x=categorical_columns['Senior Citizen'].value_counts().index, y=categorical_columns['Senior Citizen'].value_counts(), text=(categorical_columns['Senior Citizen'].value_counts()*100/categorical_columns['Senior Citizen'].shape[0]).round(2), width=[0.5, 0.5], marker={'color':colors[1]}), row=1, col=2)
    figure1.add_trace(go.Bar(x=categorical_columns['Partner'].value_counts().index, y=categorical_columns['Partner'].value_counts(), text=(categorical_columns['Partner'].value_counts()*100/categorical_columns['Partner'].shape[0]).round(2), width=[0.5, 0.5], marker={'color':colors[2]}), row=2, col=1)
    figure1.add_trace(go.Bar(x=categorical_columns['Dependents'].value_counts().index, y=categorical_columns['Dependents'].value_counts(), text=(categorical_columns['Dependents'].value_counts()*100/categorical_columns['Dependents'].shape[0]).round(2), width=[0.5, 0.5], marker={'color':colors[3]}), row=2, col=2)
    figure1.update_layout(height=750, showlegend=False)

    plotData = pd.get_dummies(data = categorical_columns[['Gender', 'Partner', 'Dependents']], columns=['Dependents']).groupby(['Gender', 'Partner']).sum().reset_index()
    figure2 = go.Figure()
    figure2.add_trace(go.Bar(
        x=plotData['Gender'],
        y=plotData['Dependents_No'],
        name='No Dependents',
        hovertext=["Partner: No", "Partner: Yes", "Partner: No", "Partner: Yes"],
        marker_color=colors[0]
    ))
    figure2.add_trace(go.Bar(
        x=plotData['Gender'],
        y=plotData['Dependents_Yes'],
        name='Dependents',
        hovertext=["Partner: No", "Partner: Yes", "Partner: No", "Partner: Yes"],
        marker_color=colors[2]
    ))

    figure3 = px.scatter(x=df['Longitude'], y=df['Latitude'], height=450, width=800, color_discrete_sequence=colors[0:2])

    with open(Global_Defs.getDemographicStatsFilePath(), 'w') as f:
        f.write(figure1.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure2.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure3.to_html(full_html=False, include_plotlyjs='cdn'))


def getCustomerAccountInformation(df):
    colors = Global_Defs.getColors()
    figure1 = make_subplots(rows=4, cols=6,
                        specs=[[{"colspan":2},None, {"colspan":2}, None, {"colspan":2}, None],
                            [{"colspan":6}, None, None, None, None, None],
                            [{"colspan":6}, None, None, None, None, None],
                            [{"colspan":6}, None, None, None, None, None]],
                            subplot_titles=['Contract Type', 'Paperless Billing Distribution', 'Payment Method', 'Tenure Months', 'Monthly Charges Distribution', 'Total Charges Distribution'],
                            horizontal_spacing=0.1)
    categorical_columns = Churn_Prediction_Utils.getCategoricalColumns(df)
    numerical_columns = Churn_Prediction_Utils.getNumericColumns(df)
    figure1.add_trace(go.Bar(x=categorical_columns['Contract'].value_counts().index, y=categorical_columns['Contract'].value_counts(), text=(categorical_columns['Contract'].value_counts()*100/categorical_columns['Contract'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[0]}), row=1, col=1)
    figure1.add_trace(go.Bar(x=categorical_columns['Paperless Billing'].value_counts().index, y=categorical_columns['Paperless Billing'].value_counts(), text=(categorical_columns['Paperless Billing'].value_counts()*100/categorical_columns['Paperless Billing'].shape[0]).round(2), width=[0.5, 0.5], marker={'color':colors[1]}), row=1, col=3)
    figure1.add_trace(go.Bar(x=categorical_columns['Payment Method'].value_counts().index, y=categorical_columns['Payment Method'].value_counts(), text=(categorical_columns['Payment Method'].value_counts()*100/categorical_columns['Payment Method'].shape[0]).round(2), width=[0.5, 0.5, 0.5, 0.5], marker={'color':colors[2]}), row=1, col=5)
    figure1.add_trace(go.Histogram(x=numerical_columns['Tenure Months'], marker={'color':colors[3]}), row=2, col=1)
    figure1.add_trace(go.Histogram(x=numerical_columns['Monthly Charges'], marker={'color':colors[4]}), row=3, col=1)
    figure1.add_trace(go.Histogram(x=numerical_columns['Total Charges'], marker={'color':colors[0]}), row=4, col=1)
    figure1.update_layout(height=1200, showlegend=False) 


    figure2 = px.histogram(df, x='Tenure Months', facet_col='Contract', height=300, color_discrete_sequence=colors[1:])

    figure3 = px.histogram(df, x='Tenure Months', facet_col='Payment Method', height=300, color_discrete_sequence=colors[2:])
    figure3.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))

    figure4 = px.scatter(numerical_columns, x='Monthly Charges', y='Total Charges', height=400, width=800, color_discrete_sequence=colors[3:])

    figure5 = px.histogram(df, x='Tenure Months', facet_col='Dependents', facet_row='Partner', height=500, color_discrete_sequence=colors[4:])

    with open(Global_Defs.getCustAccountInfoFilePath(), 'w') as f:
        f.write(figure1.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure2.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure3.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure4.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure5.to_html(full_html=False, include_plotlyjs='cdn'))

def getServiceUsageInformation(df):
    figure1 = make_subplots(rows=3, cols=3, subplot_titles= Global_Defs.getServices(), horizontal_spacing=0.1)
    categorical_columns = Churn_Prediction_Utils.getCategoricalColumns(df)
    colors = Global_Defs.getColors()
    figure1.add_trace(go.Bar(x=categorical_columns['Phone Service'].value_counts().index, y=categorical_columns['Phone Service'].value_counts(), text=(categorical_columns['Phone Service'].value_counts()*100/categorical_columns['Phone Service'].shape[0]).round(2), width=[0.5, 0.5], marker={'color':colors[0]}), row=1, col=1)
    figure1.add_trace(go.Bar(x=categorical_columns['Multiple Lines'].value_counts().index, y=categorical_columns['Multiple Lines'].value_counts(), text=(categorical_columns['Multiple Lines'].value_counts()*100/categorical_columns['Multiple Lines'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[1]}), row=1, col=2)
    figure1.add_trace(go.Bar(x=categorical_columns['Internet Service'].value_counts().index, y=categorical_columns['Internet Service'].value_counts(), text=(categorical_columns['Internet Service'].value_counts()*100/categorical_columns['Internet Service'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[2]}), row=1, col=3)
    figure1.add_trace(go.Bar(x=categorical_columns['Online Security'].value_counts().index, y=categorical_columns['Online Security'].value_counts(), text=(categorical_columns['Online Security'].value_counts()*100/categorical_columns['Online Security'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[0]}), row=2, col=1)
    figure1.add_trace(go.Bar(x=categorical_columns['Online Backup'].value_counts().index, y=categorical_columns['Online Backup'].value_counts(), text=(categorical_columns['Online Backup'].value_counts()*100/categorical_columns['Online Backup'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[1]}), row=2, col=2)
    figure1.add_trace(go.Bar(x=categorical_columns['Device Protection'].value_counts().index, y=categorical_columns['Device Protection'].value_counts(), text=(categorical_columns['Device Protection'].value_counts()*100/categorical_columns['Device Protection'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[2]}), row=2, col=3)
    figure1.add_trace(go.Bar(x=categorical_columns['Tech Support'].value_counts().index, y=categorical_columns['Tech Support'].value_counts(), text=(categorical_columns['Tech Support'].value_counts()*100/categorical_columns['Tech Support'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[0]}), row=3, col=1)
    figure1.add_trace(go.Bar(x=categorical_columns['Streaming TV'].value_counts().index, y=categorical_columns['Streaming TV'].value_counts(), text=(categorical_columns['Streaming TV'].value_counts()*100/categorical_columns['Streaming TV'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[1]}), row=3, col=2)
    figure1.add_trace(go.Bar(x=categorical_columns['Streaming Movies'].value_counts().index, y=categorical_columns['Streaming Movies'].value_counts(), text=(categorical_columns['Streaming Movies'].value_counts()*100/categorical_columns['Streaming Movies'].shape[0]).round(2), width=[0.5, 0.5, 0.5], marker={'color':colors[2]}), row=3, col=3)
    figure1.update_layout(height=750, showlegend=False)

    services = Global_Defs.getServices()
    srv_corr = []
    percent_yes = []
    percent_no = []
    for i in range(len(services)-1):
        for j in range(i+1, len(services)):
            srv_corr.append(f'{services[i]}-{services[j]}')
            percent_yes.append(categorical_columns.loc[(categorical_columns[services[i]]=='Yes') & (categorical_columns[services[j]]=='Yes')].shape[0]*100/categorical_columns.shape[0])
            percent_no.append(categorical_columns.loc[(categorical_columns[services[i]]=='No') & (categorical_columns[services[j]]=='No')].shape[0]*100/categorical_columns.shape[0])
              
    service_corr = pd.DataFrame([srv_corr, percent_yes, percent_no], index=['Service-Service', 'Yes', 'No']).T
    service_corr = service_corr.set_index('Service-Service').style.background_gradient(subset=['Yes', 'No'], cmap='bone_r')
  
    with open(Global_Defs.getServiceUsageInfoFilePath(), 'w') as f:
        f.write(figure1.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(service_corr.render())

def getCustomerChurnInformation(df):
    colors = Global_Defs.getColors()
    figure1 = px.bar(x=df['Churn Value'].value_counts().unique(),y=df['Churn Value'].value_counts(), text=(df['Churn Value'].value_counts()*100/df.shape[0]).round(2), height=400, width=600, color_discrete_sequence=colors[3:])
    categorical_columns = Churn_Prediction_Utils.getCategoricalColumns(df)

    do_dummy_cols = ['Gender', 'Partner', 'Dependents', 'Phone Service', 'Multiple Lines',
        'Internet Service', 'Online Security', 'Online Backup', 'Device Protection',
        'Tech Support', 'Streaming TV', 'Streaming Movies', 'Contract',
        'Paperless Billing', 'Payment Method']
    model_df = df.copy()
    model_df = pd.get_dummies(model_df, columns=do_dummy_cols)
    feature_corr = model_df.corr()['Churn Value'].sort_values(ascending=False)

    figure2 = px.bar(x=feature_corr.sort_values(ascending=True), y=feature_corr.sort_values(ascending=True).index, height=900, color_discrete_sequence=colors[2:])
    figure3 = px.histogram(x=df['Tenure Months'], color=df['Churn Value'], barmode='group', height=450, width=800, color_discrete_sequence=colors[1:3])
    figure4 = px.histogram(x=df['Contract'], color=df['Churn Value'], barmode='group', height=450, width=800, color_discrete_sequence=colors[2:4])
    figure5 = px.histogram(x=df['Online Security'], color=df['Churn Value'], barmode='group', height=450, width=800, color_discrete_sequence=colors[0:2])
    figure6 = px.histogram(x=df['Tech Support'], color=df['Churn Value'], barmode='group', height=450, width=800, color_discrete_sequence=colors[1:3])
    figure7 = px.histogram(x=df['Internet Service'], color=df['Churn Value'], barmode='group', height=450, width=800, color_discrete_sequence=colors[2:4])
    figure8 = px.histogram(x=df['Payment Method'], color=df['Churn Value'], barmode='group', height=450, width=800, color_discrete_sequence=colors[0:2])
    figure9 = px.scatter(x=df['Monthly Charges'], y=df['Total Charges'], color=df['Churn Value'], height=450, width=800, color_discrete_sequence=colors[1:3])
    
    figure10 = make_subplots(rows=2, cols=2, subplot_titles=['Churn Reason'])
    figure10.add_trace(go.Bar(x=categorical_columns['Churn Reason'].value_counts().index, y=categorical_columns['Churn Reason'].value_counts(), text=(categorical_columns['Churn Reason'].value_counts()*100/categorical_columns['Churn Reason'].shape[0]).round(2), width=[0.5, 0.5], marker={'color':colors[0]}), row=1, col=1)
    
    with open(Global_Defs.getCustomerChurnInfoFilePath(), 'w') as f:
        f.write(figure1.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(feature_corr.to_frame().to_html())
        f.write(figure2.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure3.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure4.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure5.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure6.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure7.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure8.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure9.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write(figure10.to_html(full_html=False, include_plotlyjs='cdn'))