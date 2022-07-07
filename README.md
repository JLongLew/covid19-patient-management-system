# COVID19 Patient Management System
Purpose: to record patients’ information and their status automatically instead of drawing a table and typing the information manually using Microsoft Word. The program has the function of registering new patients’ information, recording test results and action taken, modifying patients’ status, showing statistical information and searching patients’ data.

The program is expected to accept the input of users according each condition and record the information in each text file. It will be only available for patients who belong to one group(ATO, ACC, AEO, SID, AHS) and one zone(A, B, C, D). Group, zone and action taken for COVID-19 positive patients will be recorded using  the following abbreviation.

| Group/Zone/Action Taken                                                                 | Abbreviation |
| --------------------------------------------------------------------------------------- |:------------:|
| Asymptomatic individuals with history of travelling overseas                            |      ATO     | 
| Asymptomatic individuals who has close contact with positive patients                   |      ACC     | 
| Asymptomatic individuals who had attended event associated with known COVID-19 outbreak |      AEO     | 
| Symptomatic individuals                                                                 |      SID     | 
| Asymptomatic hospital staff                                                             |      AHS     | 
| East                                                                                    |       A      | 
| West                                                                                    |       B      | 
| North                                                                                   |       C      | 
| South                                                                                   |       D      | 
| Continue Working (Follow-Up Test Required)                                              |     CWFR     | 
| Home Quarantine (Follow-Up Test Required)                                               |     HQFR     | 
| Quarantine in Designated Centres (Follow-Up Test Required)                              |     QDFR     | 
| Home Quarantine (No Follow-Up Test Required)                                            |     HQNF     | 
| Quarantine in Hospital Normal Ward or ICU (No Follow-Up Test Required)                  |     QHNF     | 
| Allow to reunion with family                                                            |      RU      | 
| Continue Working                                                                        |      CW      | 

In this program, the patients will be required to complete three tests in 14 days to prove that he/she is totally free from COVID-19. All the patients will go through test1 as their first test and the follow-up tests will be done in series. Patients with positive test result in test1 or test2 will not need to do the following test. Patient ID and case ID will be in sequence and will include their group and zone.

Information of registered patients include patient ID, name, age, group, zone, contact number and email address will be recorded in a text file. Patients’ test details and action taken will be recorded in six text files ——— three text files for negative test result and three text files for positive test result according each test (1, 2, 3). Case ID, patient ID, zone, group and status of patients who test positive for COVID-19 will be recorded in a text file.

In the program, there will be around 20%-30% of patients test positive for COVID-19 in each test. Around 50% of patients with positive test result will be remained as active cases, around 30% of patients will be changed to recovered cases and around 20% of patients will be changed to deceased cases.
