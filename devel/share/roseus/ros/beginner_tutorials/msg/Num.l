;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::Num)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'Num (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::NUM")
  (make-package "BEGINNER_TUTORIALS::NUM"))

(in-package "ROS")
;;//! \htmlinclude Num.msg.html


(defclass beginner_tutorials::Num
  :super ros::object
  :slots (_num ))

(defmethod beginner_tutorials::Num
  (:init
   (&key
    ((:num __num) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _num __num)
   self)
  (:num
   (&optional __num)
   (if __num (setq _num __num)) _num)
  (:serialization-length
   ()
   (+
    ;; int64[] _num
    (* 8    (length _num)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64[] _num
     (write-long (length _num) s)
     (dotimes (i (length _num))
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke (elt _num i) (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class (elt _num i)) (= (length ((elt _num i) . bv)) 2)) ;; bignum
              (write-long (ash (elt ((elt _num i) . bv) 0) 0) s)
              (write-long (ash (elt ((elt _num i) . bv) 1) -1) s))
             ((and (class (elt _num i)) (= (length ((elt _num i) . bv)) 1)) ;; big1
              (write-long (elt ((elt _num i) . bv) 0) s)
              (write-long (if (>= (elt _num i) 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long (elt _num i) s)(write-long (if (>= (elt _num i) 0) 0 #xffffffff) s)))
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64[] _num
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _num (instantiate integer-vector n))
     (dotimes (i n)
#+(or :alpha :irix6 :x86_64)
      (setf (elt _num i) (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf (elt _num i) (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
     ))
   ;;
   self)
  )

(setf (get beginner_tutorials::Num :md5sum-) "fc220881caae13608159b5e38bd72534")
(setf (get beginner_tutorials::Num :datatype-) "beginner_tutorials/Num")
(setf (get beginner_tutorials::Num :definition-)
      "int64[] num

")



(provide :beginner_tutorials/Num "fc220881caae13608159b5e38bd72534")


