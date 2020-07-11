class DataFrame(object):
    # this dataframe is designed for 

    def __init__(self,start_time,end_time,sensor_list,data_matrix,is_week=True):
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.sensor_list = sensor_list
        self.sensor_num = len(sensor_list)
        self.data_matrix = data_matrix
        self.is_week = is_week



if __name__ == "__main__":
    data = DataFrame(1,1,[12,3],[13,4])
    print(data.sensor_num)
    print(data.data_matrix)