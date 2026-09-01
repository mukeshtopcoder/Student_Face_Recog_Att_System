# Test cases

| ID | Scenario | Expected result |
| --- | --- | --- |
| TC01 | Register valid student | Student and encoding are saved |
| TC02 | Register duplicate ID | Database rejects operation |
| TC03 | Recognize registered student | Correct ID is displayed |
| TC04 | Unknown face | No attendance is created |
| TC05 | Repeat same-day attendance | Duplicate is prevented |
| TC06 | Database unavailable | Clear error; no false success |
| TC07 | Invalid login | Access denied |
| TC08 | Filter report | Correct records are returned |
