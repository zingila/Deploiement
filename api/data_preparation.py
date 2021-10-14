import pandas as pd
from models import Features

gender_dict = {"Male": 0, "Female": 1}
partner_dict = {"No": 0, "Yes": 1}
dependents_dict = {"No": 0, "Yes": 1}
phoneService_dict = {"No": 0, "Yes": 1}
multipleLines_dict = {"No": 0, "Yes": 1}
internetService_dict = {
    "No": 0,
    "DSL": 1,
    "Fiber optic": 2,
}
onelineSecurity_dict = {"No": 0, "Yes": 1}
onelineBackup_dict = {"No": 0, "Yes": 1}
deviceProtection_dict = {"No": 0, "Yes": 1}
techSupport_dict = {"No": 0, "Yes": 1}
streamingTV_dict = {"No": 0, "Yes": 1}
streamingMovies_dict = {"No": 0, "Yes": 1}
contract_dict = {
    "One year": 0,
    "Two year": 1,
    "Month-to-month": 2,
}
paperslessBilling_dict = {"No": 0, "Yes": 1}
paymentMethod_dict = {
    "Credit card (automatic)": 0,
    "Bank transfer (automatic)": 1,
    "Electronic check": 2,
    "Mailed check": 3,
}
contract_dum = pd.Series(list(['One year', 'Two year', 'Month-to-month']))
paymentmethod_dum = pd.Series(list(['Credit card (automatic)', 'Bank transfer (automatic)', 'Electronic check', 'Mailed check']))
internetservice_dum = pd.Series(list(['No', 'DSL', 'Fiber optic']))

def prepare_data(data: Features):
    df = pd.DataFrame([data.dict()])
    df["SeniorCitizen"] = df["SeniorCitizen"] * 1
    df["gender"] = df["gender"].map(gender_dict)
    df["Partner"] = df["Partner"].map(partner_dict)
    df["Dependents"] = df["Dependents"].map(dependents_dict)
    df["PhoneService"] = df["PhoneService"].map(phoneService_dict)
    df["MultipleLines"] = df["MultipleLines"].map(multipleLines_dict)
    df["OnlineSecurity"] = df["OnlineSecurity"].map(onelineSecurity_dict)
    df["OnlineBackup"] = df["OnlineBackup"].map(onelineBackup_dict)
    df["DeviceProtection"] = df["DeviceProtection"].map(deviceProtection_dict)
    df["TechSupport"] = df["TechSupport"].map(techSupport_dict)
    df["StreamingTV"] = df["StreamingTV"].map(streamingTV_dict)
    df["StreamingMovies"] = df["StreamingMovies"].map(streamingMovies_dict)
    df = df.join(pd.get_dummies(df['Contract'].map(contract_dict), prefix='Contract'))
    df["PaperlessBilling"] = df["PaperlessBilling"].map(paperslessBilling_dict)
    df = df.join(pd.get_dummies(contract_dum, prefix='Contract'))
    df = df.join(pd.get_dummies(paymentmethod_dum, prefix='PaymentMethod'))
    df = df.join(pd.get_dummies(internetservice_dum, prefix='InternetService'))
    df = df.drop(['tenure', 'Contract', 'PaymentMethod', 'InternetService'], axis=1)
    #Une colonne Contract_nbr se créer alors elle est supprimée si elle existe
    if 'Contract_0' in df.columns:
        df = df.drop(['Contract_0'], axis=1)
    if 'Contract_1' in df.columns:
        df = df.drop(['Contract_1'], axis=1)
    if 'Contract_2' in df:
        df = df.drop(['Contract_2'], axis=1)
    df.info()

    return df
