import utility

def main():
    a_tmp_array,_,_,_,_ = utility.get_h5_data()
    print(a_tmp_array[0])
    print(a_tmp_array)

'''
TODO:
1. 设计dataframe的格式
2. 根据实际传感器的分布，生成distance_matrix
3. 找到温度array和实际分布的映射函数

'''

if __name__ == "__main__":
    main()