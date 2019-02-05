import rospy
from geometry_msgs.msg import Twist
pi = 3.141592654

def move1():
    
    rospy.init_node('robot_cleaner', anonymous=True)
    publisher = rospy.Publisher('/turtlebotproject/cmd_vel', Twist, queue_size=10)
    message = Twist()
    
    total_distance = 0
    total_angle = 0
    angle = input("Enter angle to be travelled in degrees:")
    

    angular_speed = input("Input angular speed (degrees/sec):")
    angular_speed = angular_speed*pi/180
    angle = angle*pi/180
    linear_speed = angular_speed*0.5
    

    message.linear.x = abs(linear_speed)
    message.angular.z = abs(angular_speed)
    
    
    message.linear.y = 0
    message.linear.z = 0
    message.angular.x = 0
    message.angular.y = 0
    
    
    while not rospy.is_shutdown():

          t0 = rospy.Time.now().to_sec()
          current_angle = 0

        
          while(current_angle < angle):
            
            publisher.publish(message)
            
            t1=rospy.Time.now().to_sec()
            
            current_angle = angular_speed*(t1-t0)
          total_distance = total_distance + linear_speed*(t1-t0)
        
          message.linear.x = 0
          message.angular.z = 0
        
          publisher.publish(message)
          angle = pi/2
          message.linear.x=0
          message.linear.y=0
          message.linear.z=0
          message.angular.x = 0
          message.angular.y = 0

    
          if (clockwise==1):
            message.angular.z = abs(angular_speed)
           else:
            message.angular.z = -abs(angular_speed)
          t2 = rospy.Time.now().to_sec()
          current_angle = 0
          while(current_angle < angle):
            
            publisher.publish(message)
            
            t3=rospy.Time.now().to_sec()
            
            current_angle = angular_speed*(t3-t2)
          message.angular.z = 0
          
          publisher.publish(message)
          distance = 1
          message.linear.x= abs(linear_speed)
          message.linear.y=0
          message.linear.z=0
          message.angular.x = 0
          message.angular.y = 0
          message.angular.z = 0
          t4 = rospy.Time.now().to_sec()
          current_distance = 0
          while(current_distance < distance):
          	publisher.publish(message)
          	t5= rospy.Time.now().to_sec()
          	current_distance = linear_speed*(t5-t4)
          message.linear.x = 0
          publisher.publish(message)
          total_distance = total_distance + current_distance
          
          message.linear.x=0
          message.linear.y=0
          message.linear.z=0
          message.angular.x = 0
          message.angular.y = 0	
          message.angular.z = -abs(angular_speed)

          t6 = rospy.Time.now().to_sec()
          current_angle = 0
          while(current_angle < angle):
            
            publisher.publish(message)
            
            t7=rospy.Time.now().to_sec()
            
            current_angle = angular_speed*(t6-t7)
          message.angular.z = 0
          publisher.publish(message)
          
          message.linear.y = 0
          message.linear.z = 0
          message.angular.x = 0
          message.angular.y = 0
          message.linear.x = -abs(linear_speed)
          message.angular.z = -abs(angular_speed)
          t8 = rospy.Time.now().to_sec()
          angle = 2*pi
          current_angle = 0

        
          while(current_angle < angle):
            
            publisher.publish(message)
            
            t9=rospy.Time.now().to_sec()
            
            current_angle = angular_speed*(t9-t8)
        
          message.linear.x = 0
          message.angular.z = 0
       
          publisher.publish(message)
          total_distance = total_distance + linear_speed(t9-t8)
          
          angle = 90*2*pi/360
          current_angle = 0
          message.angular.z = -abs(angular_speed)
          t10 = rospy.Time.now().to_sec()
          while(current_angle < angle):
            
            publisher.publish(message)
            
            t11=rospy.Time.now().to_sec()
            
            current_angle = angular_speed*(t11-t10)
          message.angular.z = 0 
          publisher.publish(message)
          
          distance = 1
          message.linear.x= -abs(linear_speed)
          message.linear.y=0
          message.linear.z=0
          message.angular.x = 0
          message.angular.y = 0
          message.angular.z = 0
          t12 = rospy.Time.now().to_sec()
          current_distance = 0
          while(current_distance < distance):
          	publisher.publish(message)
          	t13= rospy.Time.now().to_sec()
          	current_distance = linear_speed*(t13-t12)
          message.linear.x = 0
          publisher.publish(message)
          total_distance = total_distance + current_distance
          



if __name__ == '__main__':
    try:
        
        move()
    except rospy.ROSInterruptException: pass