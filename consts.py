res = 30
lat = (40.659645,40.779103)
log = (-73.989985,-73.73048)
sensor_lat = (46.51788,46.52227)
sensor_log = (6.56517,6.5693)
valid_sensor_res_10 = [8,  11,  14,  17,  19,  23,  26 ,  31,  33,  34,  35 , 40 , 46 ,  49,  51,
  55  ,57  ,59, 60,  61 , 62 ,  65 , 69 , 70 , 71 , 72 , 73 , 75 , 76 , 79 , 80 , 81,
  84  ,87 , 89 , 93 , 96 , 97 , 98 ,100, 103, 104, 109, 111, 121]
sensor_start_time_unix = 1172703600
sensor_end_time_unix = sensor_start_time_unix +7*24*3600
sensor_epoch_length = 1800
sensor_day_seconds = 86400
sensor_week_seconds = 7 * sensor_day_seconds
sensor_optimal_time_interval = 30
valid_sensor_res_10_old = [7,8,  11,  14,  17,  19,  23,  26 , 27,  31,  33,  34,  35 , 40 , 46 , 47,  49,  51,
  55  ,57  ,59,  60,  61 , 62 , 63 , 65 , 69 , 70 , 71 , 72 , 73 , 75 , 76 , 79 , 80 , 81,
  82 , 84  ,87 , 88 , 89 , 93 , 96 , 97 , 98 ,100, 103, 104, 109, 111, 121]

sensor_loc_pic = [[  0. ,  0. ,  0. ,  0. ,  0.  , 0. ,  0. ,  0.  , 0. ,  0.],
 [ 63. ,  0. ,  0. ,  0. , 42.  ,17. ,  0. ,  0.  , 0. ,  0.],
 [ 47. ,  7. , 27. ,  0. , 41.  ,56. ,121. , 46.  ,36. ,  0.],
 [  0. ,  0. ,111. , 99. , 57.  ,59. , 40. ,106.  , 0. ,  0.],
 [  0. , 61. , 71. , 65. ,  0.  ,82. , 62. ,  0.  ,76. ,  0.],
 [  0. , 51. , 11. ,122. , 68.  , 0. ,  0. , 60.  , 0. ,  0.],
 [ 84. , 81. , 55. , 72. , 73.  , 0. ,107. , 31.  ,69. , 95.],
 [103. , 80. , 96. ,  0. ,  0.  ,97. ,100. , 53.  ,19. , 93.],
 [109. , 87. ,  0. ,  0. ,104.  , 0. ,  0. ,  0.  , 0. ,  0.],
 [  0. , 89. , 88. ,  0. , 98.  , 0. ,  0. ,  0.  , 0. ,  0.],
 ]

sensor_drop_list_old = [7,27,47,63,82,88]
sensor_drop_list = [7, 27, 47,63, 55, 73,82] # optimal sensor num = 44

sensor_df_dict = {'rb_optimal':5959,'optimal':5959,'df_list':20160}
sensor_data_index = ['a_temperature_mean','a_temperature_std','a_temperature_array','sub_df_list_optimal_index','time_stamp',]
sensor_unix_column = 'Time since the epoch [s]'
sensor_idd = 'Station ID'
sensor_a_temperature = 'Ambient Temperature'
sensor_s_temperature = 'Surface Temperature'
sensor_idds_uniq = [  7 ,  8 , 11  ,14 , 17 , 19 , 23  ,26 , 27 , 31,  33  ,34  ,35 , 40 , 46,  47 , 49,  51,
  55,  57  ,59 , 60 , 61 , 62 , 63 ,65  ,69 , 70 , 71,  72,  73 , 75  ,76 , 79 , 80 , 81,
  82 , 84 , 87,  88  ,89 , 93 , 96 , 97 , 98 ,100 ,103 ,104 ,109, 111, 121]