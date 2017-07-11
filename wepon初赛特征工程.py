'''
wepon的初赛特征总结
目的：根据用户历史消费数据，预测用户是否会在规定时间内使用相应优惠券

1.ccf_offline_stage1_train.csv————用户线下消费和优惠券领取行为
特征包括：
User_id        用户ID
Merchant_id    商户ID
Coupon_id      优惠券ID：null表示无优惠券消费，此时Discount_rate和Date_received字段无意义
Discount_rate  优惠率：x \in [0,1]代表折扣率  x:y表示满x减y  单位是元
Distance     	
               用户经常活动的地点离该merchant的最近门店距离是x*500米（如果是连锁店，则取最近的一家门店）;
               x\in[0,10]；null表示无此信息，0表示低于500米，10表示大于5公里;
Date_received   领取优惠券日期
Date            消费日期：如果Date=null & Coupon_id != null，该记录表示领取优惠券但没有使用，即负样本;
                如果Date!=null & Coupon_id = null，则表示普通消费日期;
                如果Date!=null & Coupon_id != null，则表示用优惠券消费日期，即正样本;
 
2.ccf_offline_stage1_test_revised.csv————需要预测的用户线下消费和优惠券领取行为 
内容同上,少了最后一项Date

数据集划分:
                      (预测区间，取label,date_received)                              
           dateset3: 20160701~20160731 (113640),features3 from 20160315~20160630  (off_test)
           dateset2: 20160515~20160615 (258446),features2 from 20160201~20160514  
           dateset1: 20160414~20160514 (138303),features1 from 20160101~20160413 
 
############# merchant related feature   #############
1.merchant related:  商家相关的特征，在过去的数据上处理
      total_sales.       商家总消费次数
      sales_use_coupon.  商家消费中使用优惠券次数
      total_coupon       商家优惠券被领取次数
      coupon_rate = sales_use_coupon/total_sales.    使用优惠券占总销售的比值
      transfer_rate = sales_use_coupon/total_coupon. 商家优惠券被领取后使用率
      merchant_avg_distance,
      merchant_min_distance,
      merchant_max_distance of those use coupon 商家被核销优惠券中的平均/最小/最大用户-商家距离
############# coupon related feature   #############
2.coupon related: 优惠券相关的特征，在预测的数据上处理
      discount_rate.  优惠券折率
      discount_man.  满减优惠券的最低消费
      discount_jian.  满减优惠券的优惠（减）
      is_man_jian 优惠券类型(直接优惠为0, 满减为1)
      day_of_week,day_of_month. (date_received)领取优惠券是一周/一月的第几天
############# user related feature   #############
3.user related:  用户线下相关特征，在过去的数据上处理
      count_merchant.  用户消费商家数
      user_avg_distance, 
      user_min_distance,
      user_max_distance. 使用优惠券中的用户的平均/最大/最小用户-商家距离
      buy_use_coupon.    用户获得优惠券并使用次数
      buy_total.         用户消费总数
      coupon_received.   用户领取优惠券次数
      buy_use_coupon/coupon_received. 
      buy_use_coupon/buy_total
      user_date_datereceived_gap          
##################  user_merchant related feature #########################
4.user_merchant: 用户-商家交互特征，在过去的数据上处理
      user_merchant_buy_total  
      user_merchant_buy_use_coupon
      user_merchant_any
      user_merchant_buy_common
      user_merchant_coupon_transfer_rate
      user_merchant_coupon_buy_rate
      user_merchant_rate
      user_merchant_common_buy_rate
############# other feature ##################3
5. other feature:  其他特征，在预测的数据上处理
      this_month_user_receive_all_coupon_count
      this_month_user_receive_same_coupon_count
      this_month_user_receive_same_coupon_lastone
      this_month_user_receive_same_coupon_firstone
      this_day_user_receive_all_coupon_count
      this_day_user_receive_same_coupon_count
      day_gap_before, day_gap_after  (receive the same coupon)
'''
