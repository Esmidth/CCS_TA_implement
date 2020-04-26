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
| tensor1.ipynb | Empty |
| test.ipynb | Example of dealing with *data.pkl* |

## Procedure

- read csv files of lune dataset
- according to stations' GPS location, set a (lat,long) range, dividing the area to 10x10 sub areas.
- For a specific area, choose the best station with the most logs as the area readings. 
- 从整个数据集中，抽取一个子集，时间长度为一周，拥有最多的有效信号（45个）
- 在子集中，确定最小的时间间隔，可以生成最多有效的数据帧


