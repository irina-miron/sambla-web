from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler, OneHotEncoder, FunctionTransformer
import pandas as pd
import numpy as np

def make_pipe(general_scaler=RobustScaler()):
    """
    Creating pipeline for categorical data

    """

    """
    Employment type

    Transform unknow to Other and do the OHE
    """
    def log_transform(x):
        x = np.abs(x)
        return np.log(x + 1)

    transformer = FunctionTransformer(log_transform,
                                      feature_names_out='one-to-one')
    """

    Other category features that just need to one hot encode

    """
    cat_columns_ohe = ['purpose_text',
                       'application_type',
                      # 'brand',
                       'Employment_type',
                       'Civil_status',
                       'Living_arrangement_mode'
                       #,'Living_arrangement', #'Civil_status'
                      ]


    """
    Pipeline for the numerical features:

    'total_loan'
    'new_loan'
    'Monthly_income_before_tax'
    'desired_repayment_time'
    'age'

    'No__dependants'
    'No__payment_complaints'
    """

    """
    Features to transform


    desired_repayment_time: fill up with median

    """
    desired_pay_time_pipe = Pipeline([
        ('filling', SimpleImputer(strategy='median')),
        ('log_transforming', transformer),
        ('scale', general_scaler)
    ])


    """

    Normal numerical cols

    'total_loan'
    'new_loan'
    'Monthly_income_before_tax'
    'desired_repayment_time'
    'age'

    """

    num_cols = ['total_loan', 'new_loan',
                'Monthly_income_before_tax', 'desired_repayment_time_mode',
                'age', 'No__payment_complaints', 'No__dependants_mode']

    num_pipeline = Pipeline([
        ('fill', SimpleImputer(strategy='constant', fill_value=0)),
        ('log', transformer),
        ('scaling', general_scaler)
    ])

    """
    Full pipeline
    """

    pipeline= ColumnTransformer([
        #('Employment', employ_pipeline, ['Employment_type']),
        #('Living', living_pipeline, ['Living_arrangement']),
        # ('Civil status', civil_status_pipeline, ['Civil_status']),
        ('encoding', OneHotEncoder(handle_unknown='ignore',
                                   sparse_output=False), cat_columns_ohe),
        ('desired time', desired_pay_time_pipe, ['desired_repayment_time_mode']),
        # ('N dependants', n_dependants_pipe, ['No__dependants']),
        # ('N complains', n_complaiments_pipe, ['No__payment_complaints']),
        ('num features', num_pipeline, num_cols)
    ], remainder='passthrough')

    return pipeline
