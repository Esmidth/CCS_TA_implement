# CCS-TA implement

## Init

## Project Structure

### Folders

| Name| Description|
|------|--------|
|cvxpy_convex|Examples of using cvxpy library to solve convex optimization|
|Dataset|Includes Sensorscope, Air Quality Data, Rat_Sightings, Noise_Complaints_Heatmap|
|mean_png|336 Temper PNGs computed by *optimal.h5, optimal_df*  with time_gap=1800|
|more_with_less_rat|Examples of Data Conversion Procedure in paper *More with less*|
|pytorch_tutorial|Offical tutorial from Pytorch, Facebook|
|results|PNGs outputed from *Rat_Sightings* dataset, demostrate the S.T correlations|
|tensorflow1.x_tutorial|Offical tutorial of Tensorflow 1.x from Google|

### Standard Procedure for data processing

|step|program files|description|input|output|
|----|----|----|-----|----|
|1|lune copy.ipynb|read txt, generate data.h5|txt|data.h5|
|2|rename.ipynb|divide data in "data.h5" into "day1.h5" with unix_time_timestamps in a day|data.h5|day1.h5 / day2.h5|
|3|multi_process_compute.py| read day1.h5|day1.h5|dict_list3.pkl / dict_list3_1.pkl|
|3-1|lune6.ipynb| generate "optimal.h5"|data.h5|optimal.h5|
|4|read_dict_list_pkl.ipynb||dict_list3.pkl, day1.h5|sub_index_array_drop_na.pkl, sub_index_array.pkl, tensor2.pkl, time_stamp_array.pkl,indices_na.pkl, new_indices.pkl|
|??5|tensor1.ipynb||optimal_df.h5||


### Program Files

|Name|Description|
| ---- | ---- |
| consts.py | define common connst variables |
| main.py | Empty |
|**tensor_distribution.py**| Compute Tensor distribution |
|**multi_process_compute.py**| Python process pool computing example |
|test.py| Empty |
|utils.py| Utilty function |
| **esti_cs.ipynb** | Implement ESTI_CS data matrix recovery |
| loc_mapping.ipynb | Empty |
| lune copy.ipynb | export data into *data.h5, df_sub* |
| lune.ipynb | Read csv files of lune dataset, export to *data.h5, df,dfs*, find duplicated stations in a area, count NaN numbers |
| lune3.ipynb | try to get the optimal period of a week in dataset |
| lune4.ipynb | coverage_test for getting optimal sub dataset |
| lune5.ipynb | try to use multi process pool to compute coverage while there is a bug in Juypter plugin, which could not use multi process pool |
| lune6.ipynb | coverage test |
| lune7.ipynb | try to get optimal time_gap while *tensor_distribution.py* does the actual process |
| rename.ipynb | Transform data in *data.h5,df_sub* into data in *day.h5,start_point*, which starts from unix time 1162393768 |
| svd_tmp.ipynb | try to use *scipy & numpy* implementing svd |
| **tensor.ipynb** | try to build tensor used in GAN, including *remove_duplicated, dataframe_to_matrix* |
| **tensor1.ipynb** | Store data into hdf5 dataset, implement dataset_write & dataset_read function |
|tensor2.ipynb| Test dataset read & write|
|**tensor3.ipynb**| try to work with dataload in Pytorch|
|tensor4.ipynb| test Pytorch dataloader|
|tensor_prepare.ipynb| Unknown|
| test.ipynb | Example of dealing with *data.pkl* |
|**read_dict_list_pkl.ipynb**|read "dict_list3.pkl" & generate " sub_index_array.pkl" & example of using "dict_list3.pkl" |

## Procedure

- read csv files of lune dataset
- according to stations' GPS location, set a (lat,long) range, dividing the area to 10x10 sub areas.
- For a specific area, choose the best station with the most logs as the area readings.
- 从整个数据集中，抽取一个子集，时间长度为一周，拥有最多的有效信号（45个）
- 在子集中，确定最小的时间间隔，可以生成最多有效的数据帧

## Dataset

|Python Variable Name| HDF key Name |Description |Current Size|File Name|
| ---- | ---- |---|---|----|
| rb_sub_df_list_optimal | rb_optimal ||5959|ds_rb_optimal.h5|
| sub_df_list_optimal | optimal ||5959|ds_optimal.h5|
| sub_df_list | df_list ||20160|ds_df_list.h5|
| a_temperature_array |      ||5959,44|dataset.hdf5|
|a_temperature_mean|||5959|dataset.hdf5|
|a_temperature_std|||5959|dataset.hdf5|
|sub_df_list_optimal_index|||5959|dataset.hdf5|
|time_stamp|||20161|dataset.hdf5|
|dataloader|||batch_size=500|dataloader.pt|

## Thoughts

### 2020.5.2

|mission|status|
|----|---|
|dataloader重新设计，区分测试集，验证集，训练集|done|
|对数据集进行归一化处理，看看是否能改善GAN的性能|GAN只能生成归一化数据，如果将真实数据归一化，则可骗过Dis。|
|加上latent z的求导，考虑这一步的作用||
|引入部分抽样的功能||

### 2020.6.6

#### Baseline

|state-of-art|description|
|----|----|
|ARMA & SARIMA| not yet|
|stKNN|not yet|
|Kriging| done|
|AKE|done|
|DESM| delay|
|IDW+SES|done|
|CF|partial|
|NMF| done|
|NMF-MVL|not yet|
