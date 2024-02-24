endpoint = "https://learn.a3.in.th/edxphp/lms/Search/listSearchIndex"

MIME_TYPE = "application/x-www-form-urlencoded;charset=utf-8"

params = {
    "user_id": "None",
    "stext": "",
    "option": "all",
    "in_result": "",
    "aggregate": True,
    "filter": {
        "group": {
            "org": [
                # Courses based on Publisher: A3
                "IPST",  # Institute for the Promotion of Teaching Science and Technology
                "NONE-MOOC",  # None-MOOC
            ],
            "language": [
                # Courses based on language
                "th",  # Thai
                "en"  # English
            ],
            "status": [
                # Courses based on student's status
                "current",  # Current courses
                "archived"  # Archived courses
            ],
            "paced": [
                # Courses based on student's pace
                "self_paced",  # Self-paced courses
                "instructor_paced"  # Instructor-paced courses
            ],
            "sbs_subject": [
                "21000002" # วิทยาศาสตร์
                "21000004" # การงานอาชีพและเทคโนโลยี
                "21000005" # คณิตศาสตร์
            ],
            "sbs_level": [
                # Courses based on student's level
                "10000000", # ปฐมวัย
                "11000001", # ประถมศึกษา 1
                "11000002", # ประถมศึกษา 2
                "11000003", # ประถมศึกษา 3
                "11000004", # ประถมศึกษา 4
                "11000006", # ประถมศึกษา 6
                "12000001", # มัธยมศึกษาตอนต้น 1
                "12000002", # มัธยมศึกษาตอนต้น 2
                "12000003", # มัธยมศึกษาตอนต้น 3
                "12000004", # มัธยมศึกษาตอนต้น 4
                "12000005", # มัธยมศึกษาตอนต้น 5
                "12000006", # มัธยมศึกษาตอนต้น 6
                "13000001", # ปริญญาตรี
                "13000002", # ปริญญาโท
                "13000003", # ปริญญาเอก
                "14000001", # ประกาศนียบัตรวิชาชีพ (ปวช.)
                "14000002", # ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)
                "14000003", # ประกาศนียบัตรครูเทคนิคชั้นสูง (ปทส.)
                "15000000"  # การศึกษาตามอัธยาศัย
            ],
            "sbs_keywords": [
                # Courses based on keywords
                "สถิติ",    # Put the keyword here
            ],
            "sbs_pubyear": [
                # Courses based on publication year
                "2021",   # Put the year here (e.g. 2021), the display year is พ.ศ. 2564
            ],
            "sbs_course_type": [

            ]
        },
        "agg_include": True
    }
}
