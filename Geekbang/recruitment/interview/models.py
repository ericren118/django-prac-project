from django.db import models

# Create your models here.

# INTERVIEW FIRST ROUND
FIRST_INTERVIEW_RESULT_TYPE = ((u'建议复试', u'建议面试'), (u'待定', u'待定'), (u'放弃', u'放弃'))

# SUGGEST SECOND ROUND
INTERVIEW_RESULT_TYPE = ((u'建议录用', u'建议录用'), (u'待定', u'待定'), (u'放弃', u'放弃'))

# CANDIDATE EDUCATION BACKGROUND
DEGREE_TYPE = ((u'Bachelor', u'Bachelor'), (u'Master', u'Master'), (u'Phd', u'Phd'))

# HR FINAL ROUND
HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))


class Candidate(models.Model):
    # BASIC INFORMATION
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name=u'CANDIDATE ID')
    username = models.CharField(max_length=135, verbose_name=u'FULL NAME')
    city = models.CharField(max_length=135, verbose_name=u'CITY')
    phone = models.CharField(max_length=135, verbose_name=u'MOBILE')
    email = models.EmailField(max_length=135, blank=True, verbose_name=u'E-Mail')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=u'APPLIED POSITION')
    born_address = models.CharField(max_length=135, blank=True, verbose_name=u'ADDRESS')
    gender = models.CharField(max_length=135, blank=True, verbose_name=u'SEX')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name=u'OTHER INFORMATION')

    # EDUCATION BACKGROUND
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=u'BACHELOR SCHOOL')
    master_school = models.CharField(max_length=135, blank=True, verbose_name=u'MASTER SCHOOL')
    phd_school = models.CharField(max_length=135, blank=True, verbose_name=u'PHD SCHOOL')
    major = models.CharField(max_length=135, blank=True, verbose_name=u'MAJOR')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=u'DEGREE')

    # TEST SCORE
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True,
                                                        max_digits=3, blank=True,
                                                        verbose_name=u'BASIC SCORE')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3,
                                      blank=True, verbose_name=u'WRITING TEST SCORE')

    # RECORD OF FIRST INTERVIEW
    first_score = models.DecimalField(decimal_places=1, null=True,
                                      max_digits=2, blank=True, verbose_name=u'INITIAL TEST SCORE')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2,
                                                 blank=True, verbose_name=u'LEARNING ABILITY SCORE')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True,
                                                        max_digits=2, blank=True,
                                                        verbose_name=u'PROFESSIONAL ABILITY SCORE')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'ADVANTAGE')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'DISADVANTAGE')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE,
                                    blank=True, verbose_name=u'INITIAL RESULT')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'RECOMMEND POSITION')
    first_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'INTERVIEWER')
    first_remark = models.CharField(max_length=135, blank=True, verbose_name=u'FIRST REMARK')

    #  RECORD OF SECOND INTERVIEW
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2,
                                       blank=True, verbose_name=u'SECOND TEST SCORE')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2,
                                                  blank=True, verbose_name=u'LEARNING ABILITY SCORE')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2,
                                                         blank=True, verbose_name=u'PROFESSIONAL ABILITY SCORE')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2,
                                                      blank=True, verbose_name=u'PURSUE OF EXCELLENCE SCORE')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2,
                                                       blank=True, verbose_name=u'COMMUNICATION SKILL SCORE')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                verbose_name=u'ANTI PRESSURE SCORE')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'ADVANTAGE')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'DISADVANTAGE')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True,
                                     verbose_name=u'SECOND RESULT')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'RECOMMEND POSITION')
    second_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'INTERVIEWER')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name=u'SECOND REMARK')

    # FINAL INTERVIEW
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR SCORE')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE,
                                         blank=True, verbose_name=u'HR RESPONSIBILITY')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                                verbose_name=u'COMMUNICATION SKILL')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                        verbose_name=u'HR LOGIC ABILITY')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                    verbose_name='HR DEVELOPMENT POTENTIAL')
    hr_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                    verbose_name=u'HR STABILITY')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'ADVANTAGE')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'DISADVANTAGE')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True,
                                 verbose_name=u'HR FINAL RESULT')
    hr_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'HR INTERVIEWER')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name=u'HR FINAL REMARK')

    creator = models.CharField(max_length=256, blank=True, verbose_name=u'CANDIDATE DATA CREATOR')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'CREATED DATE')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u'UPDATE TIME')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name=u'LAST EDITOR')

    class Meta:
        db_table = u'candidate'
        verbose_name = u'APPLICANT'
        verbose_name_plural = u'APPLICANTS'

    def __str__(self):
        return self.username
