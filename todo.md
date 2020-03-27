# CCS_TA & More with less implement

## file structure

| filename | use  |
| -------- | ---- |
| utils.py | data import |
|      |      |


## dataset
- More with less
  -	[ ] Rat Infestation Reports
  -	[ ] Noise Complaints Heat-map
  -	[ ] Non-Employer Statistics
  -	[ ] Housing Attribute Survey
  -	[ ] Happiness
- CCS_TA
  - [x] Sensorscope
  - [ ] U-Air


## Todo List
- [x] utils.py
- [ ] 数据集的裁剪和重新保存
- [ ] 编写数据集的dataset和dataloader
- [ ] 多个batch和epoch，验证现有learning base的可用性
- [ ] 研究之所以数值的范围对不上的原因，包括learned base和重建的结果
  - [ ] latent z 是一个均值为0，正态分布的单位变量
  - [ ] l2范数标准化、l2范数归一化，数据的恢复和还原

## 进度-Sensor Scope

- [x] 分析数据集内文件和相关内容
- [x] 读取数据集并存储为HDF5文件以便快速读取
- [x] 将采集数据点聚合，创建分辨率为10*10的热力图
- [x] 去除每一个数据格中的重复项，将数据集中88个有效数据点聚合，成为50个有效数据块
- [x] 筛选一个周期为7天的数据采集时间，其短缺的数据越少越好，每个采样epoch暂定为1800s（30min）->结果是3月1日起始，drop掉(7,27,47,63,82,88)这6个数据点，共44个有效数据块
- [x] 统计每个unix秒，有几个数据帧输入->平均为2个
- [ ] 尝试构建tensor，每半个小时内的数据
- [ ] 
- [ ] 