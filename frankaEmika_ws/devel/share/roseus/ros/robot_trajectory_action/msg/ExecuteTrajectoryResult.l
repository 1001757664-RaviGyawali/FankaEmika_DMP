;; Auto-generated. Do not edit!


(when (boundp 'robot_trajectory_action::ExecuteTrajectoryResult)
  (if (not (find-package "ROBOT_TRAJECTORY_ACTION"))
    (make-package "ROBOT_TRAJECTORY_ACTION"))
  (shadow 'ExecuteTrajectoryResult (find-package "ROBOT_TRAJECTORY_ACTION")))
(unless (find-package "ROBOT_TRAJECTORY_ACTION::EXECUTETRAJECTORYRESULT")
  (make-package "ROBOT_TRAJECTORY_ACTION::EXECUTETRAJECTORYRESULT"))

(in-package "ROS")
;;//! \htmlinclude ExecuteTrajectoryResult.msg.html


(defclass robot_trajectory_action::ExecuteTrajectoryResult
  :super ros::object
  :slots (_success ))

(defmethod robot_trajectory_action::ExecuteTrajectoryResult
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get robot_trajectory_action::ExecuteTrajectoryResult :md5sum-) "358e233cde0c8a8bcfea4ce193f8fc15")
(setf (get robot_trajectory_action::ExecuteTrajectoryResult :datatype-) "robot_trajectory_action/ExecuteTrajectoryResult")
(setf (get robot_trajectory_action::ExecuteTrajectoryResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
bool success

")



(provide :robot_trajectory_action/ExecuteTrajectoryResult "358e233cde0c8a8bcfea4ce193f8fc15")


