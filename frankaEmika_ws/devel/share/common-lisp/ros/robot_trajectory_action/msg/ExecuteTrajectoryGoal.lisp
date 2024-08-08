; Auto-generated. Do not edit!


(cl:in-package robot_trajectory_action-msg)


;//! \htmlinclude ExecuteTrajectoryGoal.msg.html

(cl:defclass <ExecuteTrajectoryGoal> (roslisp-msg-protocol:ros-message)
  ((positions
    :reader positions
    :initarg :positions
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (timestamps
    :reader timestamps
    :initarg :timestamps
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass ExecuteTrajectoryGoal (<ExecuteTrajectoryGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExecuteTrajectoryGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExecuteTrajectoryGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_trajectory_action-msg:<ExecuteTrajectoryGoal> is deprecated: use robot_trajectory_action-msg:ExecuteTrajectoryGoal instead.")))

(cl:ensure-generic-function 'positions-val :lambda-list '(m))
(cl:defmethod positions-val ((m <ExecuteTrajectoryGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_trajectory_action-msg:positions-val is deprecated.  Use robot_trajectory_action-msg:positions instead.")
  (positions m))

(cl:ensure-generic-function 'timestamps-val :lambda-list '(m))
(cl:defmethod timestamps-val ((m <ExecuteTrajectoryGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_trajectory_action-msg:timestamps-val is deprecated.  Use robot_trajectory_action-msg:timestamps instead.")
  (timestamps m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExecuteTrajectoryGoal>) ostream)
  "Serializes a message object of type '<ExecuteTrajectoryGoal>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'positions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'positions))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'timestamps))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'timestamps))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExecuteTrajectoryGoal>) istream)
  "Deserializes a message object of type '<ExecuteTrajectoryGoal>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'positions) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'positions)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'timestamps) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'timestamps)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExecuteTrajectoryGoal>)))
  "Returns string type for a message object of type '<ExecuteTrajectoryGoal>"
  "robot_trajectory_action/ExecuteTrajectoryGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteTrajectoryGoal)))
  "Returns string type for a message object of type 'ExecuteTrajectoryGoal"
  "robot_trajectory_action/ExecuteTrajectoryGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExecuteTrajectoryGoal>)))
  "Returns md5sum for a message object of type '<ExecuteTrajectoryGoal>"
  "e44b206639d15eb1af20c8b932076380")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExecuteTrajectoryGoal)))
  "Returns md5sum for a message object of type 'ExecuteTrajectoryGoal"
  "e44b206639d15eb1af20c8b932076380")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExecuteTrajectoryGoal>)))
  "Returns full string definition for message of type '<ExecuteTrajectoryGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# ExecuteTrajectory.action~%~%float64[] positions~%float64[] timestamps~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExecuteTrajectoryGoal)))
  "Returns full string definition for message of type 'ExecuteTrajectoryGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# ExecuteTrajectory.action~%~%float64[] positions~%float64[] timestamps~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExecuteTrajectoryGoal>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'positions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'timestamps) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExecuteTrajectoryGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'ExecuteTrajectoryGoal
    (cl:cons ':positions (positions msg))
    (cl:cons ':timestamps (timestamps msg))
))
