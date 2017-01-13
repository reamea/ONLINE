 policy access-list acl_bronze1234_f
  seq 310 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 320 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 330 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 340 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_burst_f
  seq 310 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 320 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 330 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 340 permit ip 113.171.68.0 0.0.0.255 any class facebook
  
 policy access-list acl_subscriber_burst_cds_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

policy access-list acl_subscriber_default_f
  seq 310 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 320 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 330 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 340 permit ip 113.171.68.0 0.0.0.255 any class facebook
  
 policy access-list acl_subscriber_default_cds_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

policy access-list acl_subscriber_flat_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook
!
 policy access-list acl_subscriber_flat_peak_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_game_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_holiday_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_holiday_cds_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_nyis_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_peak_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_valuebiz_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_valuebiz2_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_valuebiz_cds_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook

 policy access-list acl_subscriber_youtube_f
  seq 430 permit ip any 183.81.30.0 0.0.0.255 class facebook
  seq 440 permit ip 183.81.30.0 0.0.0.255 any class facebook
  seq 450 permit ip any 113.171.68.0 0.0.0.255 class facebook
  seq 460 permit ip 113.171.68.0 0.0.0.255 any class facebook