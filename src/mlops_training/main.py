"""Main module."""
import numpy as np
import pandas as pd
from loguru import logger
from sklearn import datasets
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler


# Model Evaluation w/ Cross Validation
def model_eval(train, test, feature="MedHouseVal", model_id="dummy"):
    # Input: Feature & Target DataFrame

    # Split feature/target variable
    y_train = train[feature].copy()
    x_train = train.copy()
    del x_train[feature]  # remove target variable

    y_test = test[feature].copy()
    x_test = test.copy()
    del x_test[feature]

    # Pick Model
    if model_id == "dummy":
        model = DummyRegressor()
    if model_id == "rf":
        model = RandomForestRegressor(n_estimators=10, random_state=10)

    """ Parameter Based Cross Validation (No Pipeline)"""
    #     gscv = GridSearchCV(model,param_grid,cv=5)
    #     gscv.fit(X,y)
    #     results = pd.DataFrame(gscv.cv_results_)
    #     scores = np.array(results.mean_test_score).reshape(7,7)

    #     # plot the cross validation mean scores
    #     heatmap1(scores,xlabel='lamda',xticklabels=param_grid['lamd'],
    #                     ylabel='alpha',yticklabels=param_grid['alph'])

    """ Standard Cross Validation """
    cv_score = np.sqrt(-cross_val_score(model, X, y, cv=5, scoring="neg_mean_squared_error"))
    logger.info(f"Scores: {cv_score}, Mean: {cv_score.mean()}, std: {cv_score.std()}")

    preds = model.fit(x_train, y_train)
    preds = model.predict(x_test)
    test_score = mean_squared_error(y_test, preds)
    logger.info(f"Test score: {test_score}")


# function that imputes a dataframe
def impute_knn(df):
    # imputation with KNN unsupervised method

    # separate dataframe into numerical/categorical
    ldf = df.select_dtypes(include=[np.number])  # select numerical columns in df
    ldf_putaside = df.select_dtypes(exclude=[np.number])  # select categorical columns in df
    # define columns w/ and w/o missing data
    cols_nan = ldf.columns[ldf.isna().any()].tolist()  # columns w/ nan
    cols_no_nan = ldf.columns.difference(cols_nan).values  # columns w/o nan

    for col in cols_nan:
        imp_test = ldf[ldf[col].isna()]  # indicies which have missing data will become our test set
        imp_train = ldf.dropna()  # all indicies which which have no missing data
        model = KNeighborsRegressor(n_neighbors=5)  # KNR Unsupervised Approach
        knr = model.fit(imp_train[cols_no_nan], imp_train[col])
        ldf.loc[df[col].isna(), col] = knr.predict(imp_test[cols_no_nan])

    return pd.concat([ldf, ldf_putaside], axis=1)


def main():
    data = datasets.fetch_california_housing()

    df = pd.DataFrame(data=data.data, columns=data.feature_names)
    df[data["target_names"][0]] = data["target"]

    df2 = impute_knn(df)

    trdata, tedata = train_test_split(df2, test_size=0.3, random_state=42)
    trdata, tedata = trdata.copy(), tedata.copy()
    del df2, df
    # trdata_upd : training data w/ removed outliers
    maxval2 = trdata[data["target_names"][0]].max()  # get the maximum value
    trdata_upd = trdata[trdata[data["target_names"][0]] != maxval2].copy()
    tedata_upd = tedata[tedata[data["target_names"][0]] != maxval2].copy()
    # trdata_upd.hist(bins=60, figsize=(15,9),color=color1);
    # plt.show() # looks like its completely removed.

    # Make a feature that contains both longtitude & latitude
    trdata_upd["diag_coord"] = (
        trdata_upd["Longitude"] + trdata_upd["Latitude"]
    )  # 'diagonal coordinate', works for this coord

    # update test data as well
    tedata_upd["diag_coord"] = tedata_upd["Longitude"] + tedata_upd["Latitude"]

    features_cols = list(set(trdata_upd.columns) ^ {data["target_names"][0]})
    target_cols = data["target_names"][0]

    scaler = StandardScaler()
    trdata_upd[features_cols] = scaler.fit_transform(trdata_upd[features_cols])
    tedata_upd[features_cols] = scaler.transform(tedata_upd[features_cols])

    modelEval(trdata_upd, tedata_upd, model_id="dummy")
    modelEval(trdata_upd, tedata_upd, model_id="rf")

    pass


if __name__ == "__main__":
    main()
