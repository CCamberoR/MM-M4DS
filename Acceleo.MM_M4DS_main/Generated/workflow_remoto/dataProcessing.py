import pandas as pd
import functions.contract_invariants as contract_invariants
import functions.contract_pre_post as contract_pre_post
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure
class DataProcessing:
	def generateDataProcessing(self):
		pre_post=contract_pre_post.ContractsPrePost()
		invariants=contract_invariants.Invariants()
		transformations=data_transformations.DataTransformations()
#-----------------New DataProcessing-----------------
		data_model_impute_sex_in=pd.read_csv('../data_model.csv')

		missing_values_PRE_value_range_impute_sex=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_sex_in, field='sex', 
										missing_values=missing_values_PRE_value_range_impute_sex,
										quant_op=Operator(2), quant_rel=70.0/100):
			print('PRECONDITION PRE_value_range_impute_sex VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_sex NOT VALIDATED')
		
		
		print('parameter_impute_sex')
		print('Missing') #SpecialTypeInput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		
		
		missing_values_POST_value_range_impute_sex=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_sex_out, field='sex', 
										missing_values=missing_values_POST_value_range_impute_sex,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_sex VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_sex NOT VALIDATED')
		
		missing_values_INV_condition_impute_sex=[]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=data_model_impute_sex_in,
									data_dictionary_out=data_model_impute_sex_out,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_sex, axis_param=0, field='sex'):
			print('INVARIANT INV_condition_impute_sex VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_sex NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_IRSCHOOL_in=pd.read_csv('../data_model.csv')

		missing_values_PRE_value_range_impute_IRSCHOOL=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_IRSCHOOL_in, field='IRSCHOOL', 
										missing_values=missing_values_PRE_value_range_impute_IRSCHOOL,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION PRE_value_range_impute_IRSCHOOL VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_IRSCHOOL NOT VALIDATED')
		
		
		print('parameter_impute_IRSCHOOL')
		print('Missing') #SpecialTypeInput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		
		
		missing_values_POST_value_range_impute_IRSCHOOL=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_IRSCHOOL_out, field='IRSCHOOL', 
										missing_values=missing_values_POST_value_range_impute_IRSCHOOL,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_IRSCHOOL VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_IRSCHOOL NOT VALIDATED')
		
		missing_values_INV_condition_impute_IRSCHOOL=[]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=data_model_impute_IRSCHOOL_in,
									data_dictionary_out=data_model_impute_IRSCHOOL_out,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_IRSCHOOL, axis_param=0, field='IRSCHOOL'):
			print('INVARIANT INV_condition_impute_IRSCHOOL VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_IRSCHOOL NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_ETHNICITY_in=pd.read_csv('../data_model.csv')

		missing_values_PRE_value_range_impute_ETHNICITY=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_ETHNICITY_in, field='ETHNICITY', 
										missing_values=missing_values_PRE_value_range_impute_ETHNICITY,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION PRE_value_range_impute_ETHNICITY VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_ETHNICITY NOT VALIDATED')
		
		
		print('parameter_impute_ETHNICITY')
		print('Missing') #SpecialTypeInput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		
		
		missing_values_POST_value_range_impute_ETHNICITY=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_ETHNICITY_out, field='ETHNICITY', 
										missing_values=missing_values_POST_value_range_impute_ETHNICITY,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_ETHNICITY VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_ETHNICITY NOT VALIDATED')
		
		missing_values_INV_condition_impute_ETHNICITY=[]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=data_model_impute_ETHNICITY_in,
									data_dictionary_out=data_model_impute_ETHNICITY_out,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_ETHNICITY, axis_param=0, field='ETHNICITY'):
			print('INVARIANT INV_condition_impute_ETHNICITY VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_ETHNICITY NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_in=pd.read_csv('../data_model.csv')

		missing_values_PRE_value_range_impute_sex_columns=['D', 4]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_in, field='sex', 
										missing_values=missing_values_PRE_value_range_impute_sex_columns,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION PRE_value_range_impute_sex_columns VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_sex_columns NOT VALIDATED')
		
		missing_values_PRE_value_range_impute_IRSCHOOL_columns=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_in, field='IRSCHOOL', 
										missing_values=missing_values_PRE_value_range_impute_IRSCHOOL_columns,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION PRE_value_range_impute_IRSCHOOL_columns VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_IRSCHOOL_columns NOT VALIDATED')
		
		missing_values_PRE_value_range_impute_ETHNICITY_columns=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_in, field='ETHNICITY', 
										missing_values=missing_values_PRE_value_range_impute_ETHNICITY_columns,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION PRE_value_range_impute_ETHNICITY_columns VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_ETHNICITY_columns NOT VALIDATED')
		
		
		print('parameter_derivedValue_impute_mostFrequent')
		print('Missing') #SpecialTypeInput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		
		
		missing_values_POST_value_range_impute_sex_columns=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_out, field='sex', 
										missing_values=missing_values_POST_value_range_impute_sex_columns,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_sex_columns VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_sex_columns NOT VALIDATED')
		
		missing_values_POST_value_range_impute_IRSCHOOL_columns=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_out, field='IRSCHOOL', 
										missing_values=missing_values_POST_value_range_impute_IRSCHOOL_columns,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_IRSCHOOL_columns VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_IRSCHOOL_columns NOT VALIDATED')
		
		missing_values_POST_value_range_impute_ETHNICITY_columns=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_ETHNICITY_out, field='ETHNICITY', 
										missing_values=missing_values_POST_value_range_impute_ETHNICITY_columns,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_ETHNICITY_columns VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_ETHNICITY_columns NOT VALIDATED')
		
		missing_values_INV_condition_impute_sex_columns=['D', 4]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=data_model_impute_in,
									data_dictionary_out=data_model_impute_out,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_sex_columns, axis_param=0, field='sex'):
			print('INVARIANT INV_condition_impute_sex_columns VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_sex_columns NOT VALIDATED')
		
		
		missing_values_INV_condition_impute_IRSCHOOL_columns=[]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=data_model_impute_in,
									data_dictionary_out=data_model_impute_out,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_IRSCHOOL_columns, axis_param=0, field='IRSCHOOL'):
			print('INVARIANT INV_condition_impute_IRSCHOOL_columns VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_IRSCHOOL_columns NOT VALIDATED')
		
		
		missing_values_INV_condition_impute_ETHNICITY_columns=[]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=data_model_impute_in,
									data_dictionary_out=data_model_impute_out,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_ETHNICITY_columns, axis_param=0, field='ETHNICITY'):
			print('INVARIANT INV_condition_impute_ETHNICITY_columns VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_ETHNICITY_columns NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_ACADEMIC_INTEREST_2_in=pd.read_csv('../data_model.csv')

		missing_values_PRE_value_range_impute_ACADEMIC_INTEREST_2=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_ACADEMIC_INTEREST_2_in, field='ACADEMIC_INTEREST_2', 
										missing_values=missing_values_PRE_value_range_impute_ACADEMIC_INTEREST_2,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION PRE_value_range_impute_ACADEMIC_INTEREST_2 VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_ACADEMIC_INTEREST_2 NOT VALIDATED')
		
		missing_values_PRE_value_range_impute_ACADEMIC_INTEREST_1=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_ACADEMIC_INTEREST_2_in, field='ACADEMIC_INTEREST_1', 
										missing_values=missing_values_PRE_value_range_impute_ACADEMIC_INTEREST_1,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION PRE_value_range_impute_ACADEMIC_INTEREST_1 VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_ACADEMIC_INTEREST_1 NOT VALIDATED')
		
		
		print('parameter_fixValue_impute_fixValue')
		print('Missing') #SpecialTypeInput
		
		print('FixValue') #Function to call
		print('Unknown') #FixValueOutput
		data_model_impute_ACADEMIC_INTEREST_2_out=transformations.transform_special_value_fix_value(data_dictionary=data_model_impute_ACADEMIC_INTEREST_2_in, special_type_input=SpecialType(0),
																	  fix_value_output=Unknown, missing_values_list=None
								                                      data_type_output = None, axis_param=0, field = 'ACADEMIC_INTEREST_2')
		
		
		print('FixValue') #Function to call
		print('Unknown') #FixValueOutput
		data_model_impute_ACADEMIC_INTEREST_2_out=transformations.transform_special_value_fix_value(data_dictionary=data_model_impute_ACADEMIC_INTEREST_2_in, special_type_input=SpecialType(0),
																	  fix_value_output=Unknown, missing_values_list=None
								                                      data_type_output = None, axis_param=0, field = 'ACADEMIC_INTEREST_1')
		
		
		
		
		
		missing_values_POST_value_range_impute_ACADEMIC_INTEREST_2=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_ACADEMIC_INTEREST_2_out, field='ACADEMIC_INTEREST_2', 
										missing_values=missing_values_POST_value_range_impute_ACADEMIC_INTEREST_2,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_ACADEMIC_INTEREST_2 VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_ACADEMIC_INTEREST_2 NOT VALIDATED')
		
		missing_values_POST_value_range_impute_ACADEMIC_INTEREST_1=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_ACADEMIC_INTEREST_2_out, field='ACADEMIC_INTEREST_1', 
										missing_values=missing_values_POST_value_range_impute_ACADEMIC_INTEREST_1,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_ACADEMIC_INTEREST_1 VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_ACADEMIC_INTEREST_1 NOT VALIDATED')
		
		missing_values_INV_condition_impute_ACADEMIC_INTEREST_2=[]
		if invariants.check_inv_special_value_fix_value(data_dictionary_in=data_model_impute_ACADEMIC_INTEREST_2_in,
									data_dictionary_out=data_model_impute_ACADEMIC_INTEREST_2_out,
									special_type_input=SpecialType(0),
									fix_value_output='Unknown',
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									data_type_output=DataType(0),
									missing_values=missing_values_INV_condition_impute_ACADEMIC_INTEREST_2, 
									axis_param=0, field='ACADEMIC_INTEREST_2'):
			print('INVARIANT INV_condition_impute_ACADEMIC_INTEREST_2 VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_ACADEMIC_INTEREST_2 NOT VALIDATED')
		
		
		missing_values_INV_condition_impute_ACADEMIC_INTEREST_1=[]
		if invariants.check_inv_special_value_fix_value(data_dictionary_in=data_model_impute_ACADEMIC_INTEREST_2_in,
									data_dictionary_out=data_model_impute_ACADEMIC_INTEREST_2_out,
									special_type_input=SpecialType(0),
									fix_value_output='Unknown',
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									data_type_output=DataType(0),
									missing_values=missing_values_INV_condition_impute_ACADEMIC_INTEREST_1, 
									axis_param=0, field='ACADEMIC_INTEREST_1'):
			print('INVARIANT INV_condition_impute_ACADEMIC_INTEREST_1 VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_ACADEMIC_INTEREST_1 NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_mean_in=pd.read_csv('../data_model.csv')

		missing_values_PRE_value_range_impute_mean_avg_income=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_mean_in, field='avg_income', 
										missing_values=missing_values_PRE_value_range_impute_mean_avg_income,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_mean_avg_income VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_mean_avg_income NOT VALIDATED')
		
		missing_values_PRE_value_range_impute_mean_distance=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_mean_in, field='distance', 
										missing_values=missing_values_PRE_value_range_impute_mean_distance,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_mean_distance VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_mean_distance NOT VALIDATED')
		
		
		print('parameter_num_op_impute_mean')
		print('Missing') #SpecialTypeInput
		
		
		
		print('NumOp') #Function to call
		print('Mean') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Mean') #NumOpOutput
		
		
		
		missing_values_POST_value_range_impute_mean_avg_income=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_mean_out, field='avg_income', 
										missing_values=missing_values_POST_value_range_impute_mean_avg_income,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_mean_avg_income VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_mean_avg_income NOT VALIDATED')
		
		missing_values_POST_value_range_impute_mean_distance=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_mean_out, field='distance', 
										missing_values=missing_values_POST_value_range_impute_mean_distance,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_mean_distance VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_mean_distance NOT VALIDATED')
		
		missing_values_INV_condition_avg_income=[]
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_mean_in,
												data_dictionary_out=data_model_impute_mean_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(0),
												num_op_output=Operation(1),
												missing_values=missing_values_INV_condition_avg_income, axis_param=0, field='avg_income'):
			print('INVARIANT INV_condition_avg_income VALIDATED')
		else:
			print('INVARIANT INV_condition_avg_income NOT VALIDATED')
		
		
		missing_values_INV_condition_distance=[]
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_mean_in,
												data_dictionary_out=data_model_impute_mean_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(0),
												num_op_output=Operation(1),
												missing_values=missing_values_INV_condition_distance, axis_param=0, field='distance'):
			print('INVARIANT INV_condition_distance VALIDATED')
		else:
			print('INVARIANT INV_condition_distance NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_linear_interpolation_in=pd.read_csv('../data_model.csv')

		missing_values_PRE_value_range_impute_linear_interpolation_satscore=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=data_model_impute_linear_interpolation_in, field='satscore', 
										missing_values=missing_values_PRE_value_range_impute_linear_interpolation_satscore,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_linear_interpolation_satscore VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_linear_interpolation_satscore NOT VALIDATED')
		
		
		print('parameter_num_op_impute_mean')
		print('Missing') #SpecialTypeInput
		
		
		
		print('NumOp') #Function to call
		print('Mean') #NumOpOutput
		
		
		
		missing_values_POST_value_range_impute_linear_interpolation_satscore=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=data_model_impute_linear_interpolation_out, field='satscore', 
										missing_values=missing_values_POST_value_range_impute_linear_interpolation_satscore,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_linear_interpolation_satscore VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_linear_interpolation_satscore NOT VALIDATED')
		
		missing_values_INV_condition_distance=[]
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_linear_interpolation_in,
												data_dictionary_out=data_model_impute_linear_interpolation_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(0),
												num_op_output=Operation(0),
												missing_values=missing_values_INV_condition_distance, axis_param=0, field='satscore'):
			print('INVARIANT INV_condition_distance VALIDATED')
		else:
			print('INVARIANT INV_condition_distance NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_row_filter_in=pd.read_csv('../workflow_datasets/data_model_impute_out.csv')

		if pre_post.check_fix_value_range(value=0, data_dictionary=data_model_row_filter_in, belong_op=Belong(0), field='init_span',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_row_filter VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_row_filter NOT VALIDATED')
		
		
		
		
		
		if pre_post.check_fix_value_range(value='0', data_dictionary=data_model_row_filter_out, belong_op=Belong(1), field='init_span',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_row_filter VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_row_filter NOT VALIDATED')
		
#-----------------New DataProcessing-----------------
		data_model_column_cont_filter_in=pd.read_csv('../workflow_datasets/data_model_row_filter_out.csv')

		field_list_PRE_field_range_column_cont_filter=['TRAVEL_INIT_CNTCTS', 'REFERRAL_CNCTS', 'telecq', 'stuemail', 'interest']
		if pre_post.check_field_range(fields=field_list_PRE_field_range_column_cont_filter,
									data_dictionary=data_model_column_cont_filter_in,
									belong_op=Belong(0)):
			print('PRECONDITION PRE_field_range_column_cont_filter VALIDATED')
		else:
			print('PRECONDITION PRE_field_range_column_cont_filter NOT VALIDATED')
		
		
		
		
		
		
		field_list_POST_field_range_column_cont_filter=['stuemail', 'interest', 'telecq', 'TRAVEL_INIT_CNTCTS', 'REFERRAL_CNCTS']
		if pre_post.check_field_range(fields=field_list_POST_field_range_column_cont_filter,
									data_dictionary=data_model_column_cont_filter_out,
									belong_op=Belong(1)):
			print('POSTCONDITION POST_field_range_column_cont_filter VALIDATED')
		else:
			print('POSTCONDITION POST_field_range_column_cont_filter NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_column_cat_filter_in=pd.read_csv('../workflow_datasets/data_model_row_filter_out.csv')

		field_list_PRE_field_range_column_cat_filter=['CONTACT_CODE1']
		if pre_post.check_field_range(fields=field_list_PRE_field_range_column_cat_filter,
									data_dictionary=data_model_column_cat_filter_in,
									belong_op=Belong(0)):
			print('PRECONDITION PRE_field_range_column_cat_filter VALIDATED')
		else:
			print('PRECONDITION PRE_field_range_column_cat_filter NOT VALIDATED')
		
		
		
		
		
		
		field_list_POST_field_range_column_cat_filter=['CONTACT_CODE1']
		if pre_post.check_field_range(fields=field_list_POST_field_range_column_cat_filter,
									data_dictionary=data_model_column_cat_filter_out,
									belong_op=Belong(1)):
			print('POSTCONDITION POST_field_range_column_cat_filter VALIDATED')
		else:
			print('POSTCONDITION POST_field_range_column_cat_filter NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_map_territory_in=pd.read_csv('../workflow_datasets/data_model_col_filter_out.csv')

		if pre_post.check_fix_value_range(value='A', data_dictionary=data_model_map_territory_in, belong_op=Belong(0), field='TERRITORY',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_territory VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_territory NOT VALIDATED')
		if pre_post.check_fix_value_range(value='N', data_dictionary=data_model_map_territory_in, belong_op=Belong(0), field='TERRITORY',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_territory VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_territory NOT VALIDATED')
		
		
		print('Transformation of type FixValue-FixValue')
		
		input_values_list_parameter_map_territory_A=['A', 'N']
		output_values_list_parameter_map_territory_A=['0', '0']
		data_type_input_list_parameter_map_territory_A=[DataType(0), DataType(0)]
		data_type_output_list_parameter_map_territory_A=[DataType(0), DataType(0)]
		
		
		data_model_map_territory_out=transformations.transform_fix_value_fix_value(data_dictionary=data_model_map_territory_in, input_values_list=input_values_list_parameter_map_territory_A,
																	  output_values_list=output_values_list_parameter_map_territory_A,
								                                      data_type_input_list = data_type_input_list_parameter_map_territory_A,
								                                      data_type_output_list = data_type_output_list_parameter_map_territory_A, field = 'TERRITORY')
		
		
		
		if pre_post.check_fix_value_range(value='A', data_dictionary=data_model_map_territory_out, belong_op=Belong(0), field='TERRITORY',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_territory VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_territory NOT VALIDATED')
		if pre_post.check_fix_value_range(value='N', data_dictionary=data_model_map_territory_out, belong_op=Belong(0), field='TERRITORY',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_territory VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_territory NOT VALIDATED')
		
		
		input_values_list_INV_condition_map_categorical_col=['A', 'B', 'N']
		output_values_list_INV_condition_map_categorical_col=['0', '0', '0']
		
		data_type_input_list_INV_condition_map_categorical_col=[DataType(0), DataType(0), DataType(0)]
		data_type_output_list_INV_condition_map_categorical_col=[DataType(0), DataType(0), DataType(0)]
		
		if invariants.check_inv_fix_value_fix_value(data_dictionary_in=data_model_map_territory_in,
												data_dictionary_out=data_model_map_territory_out,
												input_values_list=input_values_list_INV_condition_map_categorical_col, 
												output_values_list=output_values_list_INV_condition_map_categorical_col,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												data_type_input_list=data_type_input_list_INV_condition_map_categorical_col,
												data_type_output_list=data_type_output_list_INV_condition_map_categorical_col,
												field='TERRITORY'):
			print('INVARIANT INV_condition_map_categorical_col VALIDATED')
		else:
			print('INVARIANT INV_condition_map_categorical_col NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_map_Instate_in=pd.read_csv('../workflow_datasets/data_model_map_territory_out.csv')

		if pre_post.check_fix_value_range(value='Y', data_dictionary=data_model_map_Instate_in, belong_op=Belong(0), field='Instate',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_Instate VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_Instate NOT VALIDATED')
		if pre_post.check_fix_value_range(value='N', data_dictionary=data_model_map_Instate_in, belong_op=Belong(0), field='Instate',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_Instate VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_Instate NOT VALIDATED')
		
		
		input_values_list_INV_condition_map_categorical_col=['Y', 'N']
		output_values_list_INV_condition_map_categorical_col=['1', '0']
		
		data_type_input_list_INV_condition_map_categorical_col=[DataType(0), DataType(0)]
		data_type_output_list_INV_condition_map_categorical_col=[DataType(0), DataType(0)]
		
		if invariants.check_inv_fix_value_fix_value(data_dictionary_in=data_model_map_Instate_in,
												data_dictionary_out=data_model_map_Instate_out,
												input_values_list=input_values_list_INV_condition_map_categorical_col, 
												output_values_list=output_values_list_INV_condition_map_categorical_col,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												data_type_input_list=data_type_input_list_INV_condition_map_categorical_col,
												data_type_output_list=data_type_output_list_INV_condition_map_categorical_col,
												field='Instate'):
			print('PRECONDITION INV_condition_map_categorical_col VALIDATED')
		else:
			print('PRECONDITION INV_condition_map_categorical_col NOT VALIDATED')
		
		
		
		print('Transformation of type FixValue-FixValue')
		
		input_values_list_parameter_map_instate_Y=['Y', 'N']
		output_values_list_parameter_map_instate_Y=['1', '0']
		data_type_input_list_parameter_map_instate_Y=[DataType(0), DataType(0)]
		data_type_output_list_parameter_map_instate_Y=[DataType(0), DataType(0)]
		
		
		data_model_map_Instate_out=transformations.transform_fix_value_fix_value(data_dictionary=data_model_map_Instate_in, input_values_list=input_values_list_parameter_map_instate_Y,
																	  output_values_list=output_values_list_parameter_map_instate_Y,
								                                      data_type_input_list = data_type_input_list_parameter_map_instate_Y,
								                                      data_type_output_list = data_type_output_list_parameter_map_instate_Y, field = 'Instate')
		
		
		
		if pre_post.check_fix_value_range(value='Y', data_dictionary=data_model_map_Instate_out, belong_op=Belong(0), field='Instate',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_Instate VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_Instate NOT VALIDATED')
		if pre_post.check_fix_value_range(value='N', data_dictionary=data_model_map_Instate_out, belong_op=Belong(0), field='Instate',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_Instate VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_Instate NOT VALIDATED')
		
#-----------------New DataProcessing-----------------
		data_model_stringToNumber_in=pd.read_csv('../workflow_datasets/data_model_map_instate_out.csv')

		
		
		
		
		if invariants.check_inv_missing_value_missing_value(data_dictionary_in=data_model_stringToNumber_in,
												data_dictionary_out=data_model_stringToNumber_out,
												belong_op_out=Belong(1), field='TERRITORY'):
			print('INVARIANT INV_condition_TERRITORY VALIDATED')
		else:
			print('INVARIANT INV_condition_TERRITORY NOT VALIDATED')
		
		
		if invariants.check_inv_missing_value_missing_value(data_dictionary_in=data_model_stringToNumber_in,
												data_dictionary_out=data_model_stringToNumber_out,
												belong_op_out=Belong(1), field='init1rat'):
			print('INVARIANT INV_condition_init1rat VALIDATED')
		else:
			print('INVARIANT INV_condition_init1rat NOT VALIDATED')
		
		
		if invariants.check_inv_missing_value_missing_value(data_dictionary_in=data_model_stringToNumber_in,
												data_dictionary_out=data_model_stringToNumber_out,
												belong_op_out=Belong(1), field='init2rat'):
			print('INVARIANT INV_condition_init2rat VALIDATED')
		else:
			print('INVARIANT INV_condition_init2rat NOT VALIDATED')
		
		
		if invariants.check_inv_missing_value_missing_value(data_dictionary_in=data_model_stringToNumber_in,
												data_dictionary_out=data_model_stringToNumber_out,
												belong_op_out=Belong(1), field='hscrat'):
			print('INVARIANT INV_condition_hscrat VALIDATED')
		else:
			print('INVARIANT INV_condition_hscrat NOT VALIDATED')
		
		
		if invariants.check_inv_missing_value_missing_value(data_dictionary_in=data_model_stringToNumber_in,
												data_dictionary_out=data_model_stringToNumber_out,
												belong_op_out=Belong(1), field='Instate'):
			print('INVARIANT INV_condition_Instate VALIDATED')
		else:
			print('INVARIANT INV_condition_Instate NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_outlier_closest_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')

		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=data_model_impute_outlier_closest_in, field='avg_income', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_outliers_closest_avg_income VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_outliers_closest_avg_income NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=data_model_impute_outlier_closest_in, field='distance', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_outliers_closest_distance VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_outliers_closest_distance NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=data_model_impute_outlier_closest_in, field='premiere', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_outliers_closest_premiere VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_outliers_closest_premiere NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=data_model_impute_outlier_closest_in, field='sex', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_outliers_closest_sex VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_outliers_closest_sex NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=data_model_impute_outlier_closest_in, field='Enroll', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_outliers_closest_Enroll VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_outliers_closest_Enroll NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=data_model_impute_outlier_closest_in, field='Instate', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION PRE_value_range_impute_outliers_closest_Instate VALIDATED')
		else:
			print('PRECONDITION PRE_value_range_impute_outliers_closest_Instate NOT VALIDATED')
		
		
		print('parameter_num_op_impute_mean')
		print('Outlier') #SpecialTypeInput
		
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=data_model_impute_outlier_closest_out, field='avg_income', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_outliers_closest_avg_income VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_outliers_closest_avg_income NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=data_model_impute_outlier_closest_out, field='distance', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_outliers_closest_distance VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_outliers_closest_distance NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=data_model_impute_outlier_closest_in, field='premiere', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_outliers_closest_premiere VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_outliers_closest_premiere NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=data_model_impute_outlier_closest_out, field='sex', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_outliers_closest_sex VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_outliers_closest_sex NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=data_model_impute_outlier_closest_out, field='Enroll', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_outliers_closest_Enroll VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_outliers_closest_Enroll NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=data_model_impute_outlier_closest_out, field='Instate', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_outliers_closest_Instate VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_outliers_closest_Instate NOT VALIDATED')
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_outlier_closest_in,
												data_dictionary_out=data_model_impute_outlier_closest_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='avg_income'):
			print('INVARIANT INV_condition_avg_income VALIDATED')
		else:
			print('INVARIANT INV_condition_avg_income NOT VALIDATED')
		
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_outlier_closest_in,
												data_dictionary_out=data_model_impute_outlier_closest_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='distance'):
			print('INVARIANT INV_condition_distance VALIDATED')
		else:
			print('INVARIANT INV_condition_distance NOT VALIDATED')
		
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_outlier_closest_in,
												data_dictionary_out=data_model_impute_outlier_closest_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='premiere'):
			print('INVARIANT INV_condition_premiere VALIDATED')
		else:
			print('INVARIANT INV_condition_premiere NOT VALIDATED')
		
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_outlier_closest_in,
												data_dictionary_out=data_model_impute_outlier_closest_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='sex'):
			print('INVARIANT INV_condition_sex VALIDATED')
		else:
			print('INVARIANT INV_condition_sex NOT VALIDATED')
		
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_outlier_closest_in,
												data_dictionary_out=data_model_impute_outlier_closest_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='Enroll'):
			print('INVARIANT INV_condition_Enroll VALIDATED')
		else:
			print('INVARIANT INV_condition_Enroll NOT VALIDATED')
		
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=data_model_impute_outlier_closest_in,
												data_dictionary_out=data_model_impute_outlier_closest_out,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='Instate'):
			print('INVARIANT INV_condition_Instate VALIDATED')
		else:
			print('INVARIANT INV_condition_Instate NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_binner_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')

		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=data_model_binner_in,
		                                	closure_type=Closure(0), belong_op=Belong(0), field='TOTAL_CONTACTS'):
			print('PRECONDITION PRE_binner_valueRange_TOTAL_CONTACTS VALIDATED')
		else:
			print('PRECONDITION PRE_binner_valueRange_TOTAL_CONTACTS NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=data_model_binner_in,
		                                	closure_type=Closure(0), belong_op=Belong(0), field='SELF_INIT_CNTCTS'):
			print('PRECONDITION PRE_binner_valueRange_SELF_INIT_CNTCTS VALIDATED')
		else:
			print('PRECONDITION PRE_binner_valueRange_SELF_INIT_CNTCTS NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=data_model_binner_in,
		                                	closure_type=Closure(0), belong_op=Belong(0), field='SOLICITED_CNTCTS'):
			print('PRECONDITION PRE_binner_valueRange_SOLICITED_CNTCTS VALIDATED')
		else:
			print('PRECONDITION PRE_binner_valueRange_SOLICITED_CNTCTS NOT VALIDATED')
		
		
		
		
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=data_model_binner_out,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='TOTAL_CONTACTS_binned'):
			print('POSTCONDITION POST_binner_valueRange_TOTAL_CONTACTS VALIDATED')
		else:
			print('POSTCONDITION POST_binner_valueRange_TOTAL_CONTACTS NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=data_model_binner_out,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='SELF_INIT_CNTCTS_binned'):
			print('POSTCONDITION POST_binner_valueRange_SELF_INIT_CNTCTS VALIDATED')
		else:
			print('POSTCONDITION POST_binner_valueRange_SELF_INIT_CNTCTS NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=data_model_binner_in,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='SOLICITED_CNTCTS'):
			print('POSTCONDITION POST_binner_valueRange_SOLICITED_CNTCTS VALIDATED')
		else:
			print('POSTCONDITION POST_binner_valueRange_SOLICITED_CNTCTS NOT VALIDATED')
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=-1000.0, right_margin=1.0,
												closure_type=Closure(0),
												fix_value_output='Low',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TOTAL_CONTACTS'):
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=1.0, right_margin=4.0,
												closure_type=Closure(2),
												fix_value_output='Moderate',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TOTAL_CONTACTS'):
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=4.0, right_margin=1000.0,
												closure_type=Closure(2),
												fix_value_output='High',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TOTAL_CONTACTS'):
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS NOT VALIDATED')
		
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=-1000.0, right_margin=1.0,
												closure_type=Closure(0),
												fix_value_output='Low',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SELF_INIT_CNTCTS'):
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=1.0, right_margin=4.0,
												closure_type=Closure(2),
												fix_value_output='Moderate',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SELF_INIT_CNTCTS'):
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=4.0, right_margin=1000.0,
												closure_type=Closure(2),
												fix_value_output='High',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SELF_INIT_CNTCTS'):
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS NOT VALIDATED')
		
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=-1000.0, right_margin=1.0,
												closure_type=Closure(0),
												fix_value_output='Low',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SOLICITED_CNTCTS'):
			print('INVARIANT INV_binner_condition_SOLICITED_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SOLICITED_CNTCTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=1.0, right_margin=4.0,
												closure_type=Closure(2),
												fix_value_output='Moderate',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SOLICITED_CNTCTS'):
			print('INVARIANT INV_binner_condition_SOLICITED_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SOLICITED_CNTCTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=4.0, right_margin=1000.0,
												closure_type=Closure(2),
												fix_value_output='High',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SOLICITED_CNTCTS'):
			print('INVARIANT INV_binner_condition_SOLICITED_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SOLICITED_CNTCTS NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		data_model_binner_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')

		if pre_post.check_interval_range_float(left_margin=0.0, right_margin=1000.0, data_dictionary=data_model_binner_in,
		                                	closure_type=Closure(3), belong_op=Belong(0), field='TERRITORY'):
			print('PRECONDITION PRE_binner_valueRange_TERRITORY VALIDATED')
		else:
			print('PRECONDITION PRE_binner_valueRange_TERRITORY NOT VALIDATED')
		
		
		
		
		
		if pre_post.check_interval_range_float(left_margin=0.0, right_margin=1000.0, data_dictionary=data_model_binner_out,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='TERRITORY_binned'):
			print('POSTCONDITION POST_binner_valueRange_TERRITORY VALIDATED')
		else:
			print('POSTCONDITION POST_binner_valueRange_TERRITORY NOT VALIDATED')
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=-1000.0, right_margin=1.0,
												closure_type=Closure(0),
												fix_value_output='Unknown',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=1.0, right_margin=3.0,
												closure_type=Closure(2),
												fix_value_output='Zone 1',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=3.0, right_margin=5.0,
												closure_type=Closure(2),
												fix_value_output='Zone 2',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=5.0, right_margin=7.0,
												closure_type=Closure(2),
												fix_value_output='Zone 3',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=data_model_binner_in,
												data_dictionary_out=data_model_binner_out,
												left_margin=7.0, right_margin=1000.0,
												closure_type=Closure(2),
												fix_value_output='Zone 4',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_TOTAL_CONTACTS NOT VALIDATED')
		
		















dp=DataProcessing()
dp.generateDataProcessing()
