from django.db import models

from .master_models import ProcessMaster
from .master_models import PressureUnitMaster, AmountUnitMaster
from .master_models import WorkClassMaster, ExchangeTypeMaster
from .master_models import PlanClassMaster
from .common_master_models import DepartmentMaster, User


# 工事
class Work(models.Model):
    work_id = models.IntegerField('工事id', blank=True, null=True)
    work_rev_no = models.IntegerField('RevNo', blank=True, null=True)
    work_budget_id = models.IntegerField('予算id', blank=True, null=True)
    work_name = models.CharField('工事名', max_length=70, blank=True, null=True)
    work_charge_process = models.ForeignKey(ProcessMaster, verbose_name='設備工程', null=True, on_delete=models.PROTECT)
    work_class = models.ForeignKey(WorkClassMaster, verbose_name='物品/工事区分', null=True, on_delete=models.PROTECT)
    management_class_cd = models.CharField('管理区分CD', max_length=2, blank=True, null=True)
    work_order_department = models.ForeignKey(DepartmentMaster, verbose_name='部署', null=True, on_delete=models.PROTECT)
    work_order_department_charge_person = models.ForeignKey(User, related_name='work_order_department_charge_users', verbose_name='原課担当者', on_delete=models.PROTECT,null=True)
    work_planning_charge_person = models.ForeignKey(User, related_name='work_planning_charge_users', verbose_name='計画担当者', on_delete=models.PROTECT, null=True)
    work_execution_charge_person = models.ForeignKey(User, related_name='work_execution_charge_users', verbose_name='実行担当者', on_delete=models.PROTECT, null=True)
    work_required_function = models.CharField('要求機能', max_length=20, blank=True, null=True)
    sub_no = models.IntegerField('サブNo', blank=True, null=True)
    delivery_location = models.CharField('納入先', max_length=40, blank=True, null=True)
    work_start_date = models.DateField('着工日', blank=True, null=True)
    work_end_date = models.DateField('完工日', blank=True, null=True)
    work_delivery_date = models.DateField('納期日', blank=True, null=True)
    estimate_date = models.DateField('見積提出希望日', blank=True, null=True)
    work_estimate_limited_date = models.DateField('見積提出期限', blank=True, null=True)
    work_question_limited_date = models.DateField('質問受付期日', blank=True, null=True)
    work_answer_limited_date = models.DateField('質問回答期日', blank=True, null=True)
    make_limited_date = models.DateField('本仕様書作成期日', blank=True, null=True)
    order_limited_date = models.DateField('発注期日', blank=True, null=True)
    fixed_form = models.CharField('定型_非定型', max_length=50, blank=True, null=True)
    estimate_range = models.TextField('見積範囲', max_length=400, blank=True, null=True)
    budget_material = models.IntegerField('取扱い物質', blank=True, null=True)
    confidentiality = models.TextField('秘密保持条件', max_length=4000, blank=True, null=True)
    warranty = models.TextField('瑕疵担保責任', max_length=4000, blank=True, null=True)
    acceptance_conditions = models.TextField('検収条件', max_length=4000, blank=True, null=True)
    witness_inspection = models.IntegerField('立会検査有無', blank=True, null=True)
    acceptance_inspection = models.IntegerField('受入検査有無', blank=True, null=True)
    test_run = models.IntegerField('試運転有無', blank=True, null=True)
    test_run_pass = models.TextField('試運転の合格基準', max_length=4000, blank=True, null=True)
    inspection_period = models.TextField('検査の期間', max_length=4000, blank=True, null=True)
    Attachment_url = models.URLField('添付資料格納', max_length=400, blank=True, null=True)
    work_rem = models.TextField('備考', max_length=400, blank=True, null=True)
    plan_class = models.ForeignKey(PlanClassMaster, verbose_name='計画区分', null=True, on_delete=models.PROTECT)
    last_plan_id = models.IntegerField('前計画区分工事ID', blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)
    cancel_flag = models.IntegerField('中止FL', blank=True, null=True)
    entry_on_progress_flag = models.IntegerField('登録中FL', blank=True, null=True)
    entry_datetime = models.DateTimeField('登録日時', blank=True, null=True)
    entry_operator = models.CharField('登録者', max_length=20, blank=True, null=True)
    update_datetime = models.DateTimeField('更新日時', blank=True, null=True)
    update_operator = models.CharField('変更者', max_length=20, blank=True, null=True)


# 詳細仕様_機械_熱交換機
class WorkSpecMEX(models.Model):
    work_id = models.IntegerField('工事id', blank=True, null=True)
    rev_no = models.IntegerField('RevNo', blank=True, null=True)
    required_function_id = models.IntegerField('要求機能id', blank=True, null=True)
    exchange_capacity = models.FloatField('交換熱量', blank=True, null=True)
    exchange_type = models.ForeignKey(ExchangeTypeMaster, verbose_name='型式', null=True, on_delete=models.PROTECT)
    exchange_area = models.FloatField('伝熱面積', blank=True, null=True)
    hot_fluid = models.CharField('高温物質', max_length=40, blank=True, null=True)
    hot_design_temperature = models.FloatField('高温側設計温度', blank=True, null=True)
    hot_regular_use_temperature = models.FloatField('高温側常用温度', blank=True, null=True)
    hot_input_temperature = models.FloatField('高温側入口温度', blank=True, null=True)
    hot_output_temperature = models.FloatField('高温側出口温度', blank=True, null=True)
    hot_fluid_capacity = models.FloatField('高温物質流量', blank=True, null=True)
    hot_fluid_capacity_unit = models.ForeignKey(AmountUnitMaster, related_name='hot_fluid_capacity_unit', verbose_name='高温物質流量単位', on_delete=models.PROTECT)
    hot_design_pressure = models.FloatField('高温側設計圧力', blank=True, null=True)
    hot_regular_use_pressure = models.FloatField('高温側常用圧力', blank=True, null=True)
    hot_pressure_unit = models.ForeignKey(PressureUnitMaster, related_name='hot_pressure_unit', verbose_name='圧力単位', on_delete=models.PROTECT)
    cool_fluid = models.CharField('低温物質', max_length=40, blank=True, null=True)
    cool_design_temperature = models.FloatField('低温側設計温度', blank=True, null=True)
    cool_regular_use_temperature = models.FloatField('低温側常用温度', blank=True, null=True)
    cool_input_temperature = models.FloatField('低温側入口温度', blank=True, null=True)
    cool_output_use_temperature = models.FloatField('低温側出口温度', blank=True, null=True)
    cool_fluid_capacity = models.FloatField('低温物質流量', blank=True, null=True)
    cool_fluid_capacity_unit = models.ForeignKey(AmountUnitMaster, related_name='cool_fluid_capacity_unit', verbose_name='低温物質流量単位', on_delete=models.PROTECT)
    cool_design_pressure = models.FloatField('低温側設計圧力', blank=True, null=True)
    cool_regular_use_pressure = models.FloatField('低温側常用圧力', blank=True, null=True)
    cool_pressure_unit = models.ForeignKey(PressureUnitMaster, related_name='cool_pressure_unit', verbose_name='圧力単位', on_delete=models.PROTECT)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)
    entry_on_progress_flag = models.IntegerField('登録中FL', blank=True, null=True)
    entry_datetime = models.DateTimeField('登録日時', blank=True, null=True)
    entry_operator = models.CharField('登録者', max_length=20, blank=True, null=True)
    update_datetime = models.DateTimeField('更新日時', blank=True, null=True)
    update_operator = models.CharField('変更者', max_length=20, blank=True, null=True)
    required_function_sub_no = models.IntegerField('要求機能サブNO', blank=True, null=True)
    entry_class = models.CharField('登録区分', max_length=20, blank=True, null=True)
    heat_exchange_rem = models.TextField('備考', max_length=400, blank=True, null=True)


# 詳細仕様_機械_貯蔵
class WorkSpecMVE(models.Model):
    work_id = models.IntegerField('工事id', blank=True, null=True)
    rev_no = models.IntegerField('RevNo', blank=True, null=True)
    required_function_id = models.IntegerField('要求仕様id', blank=True, null=True)
    stock_material = models.CharField('物質', max_length=40, blank=True, null=True)
    stock_capacity = models.FloatField('貯蔵量', blank=True, null=True)
    stock_capacity_unit = models.ForeignKey(AmountUnitMaster, verbose_name='貯蔵量単位', null=True, on_delete=models.PROTECT)
    design_pressure = models.FloatField('設計圧力', blank=True, null=True)
    regular_use_pressure = models.FloatField('常用圧力', blank=True, null=True)
    pressure_unit = models.ForeignKey(PressureUnitMaster, verbose_name='圧力単位', null=True, on_delete=models.PROTECT)
    design_temperature = models.FloatField('設計温度', blank=True, null=True)
    regular_use_temperature = models.FloatField('常用温度', blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)
    entry_on_progress_flag = models.IntegerField('登録中FL', blank=True, null=True)
    entry_datetime = models.DateTimeField('登録日時', blank=True, null=True)
    entry_operator = models.CharField('登録者', max_length=20, blank=True, null=True)
    update_datetime = models.DateTimeField('更新日時', blank=True, null=True)
    update_operator = models.CharField('変更者', max_length=20, blank=True, null=True)
    required_function_sub_no = models.IntegerField('要求機能サブNO', blank=True, null=True)
    entry_class = models.CharField('登録区分', max_length=20, blank=True, null=True)
    vessel_rem = models.TextField('備考', max_length=400, blank=True, null=True)


# 工事関係機器
class WorkEquipment(models.Model):
    budget_id = models.IntegerField('予算id', blank=True, null=True)
    work_id = models.IntegerField('工事id', blank=True, null=True)
    rev_no = models.IntegerField('RevNo', blank=True, null=True)
    equip_no = models.CharField('機器NO', max_length=50, blank=True, null=True)
    equip_name = models.CharField('機器名', max_length=100, blank=True, null=True)
    management_class = models.CharField('区分', max_length=50, blank=True, null=True)
    facility = models.CharField('設備工程', max_length=50, blank=True, null=True)
    equipment_purchase = models.IntegerField('機器購入', blank=True, null=True)
    construction = models.IntegerField('工事', blank=True, null=True)
    equip_family = models.CharField('機器ファミリー', max_length=50, blank=True, null=True)
    equip_type = models.CharField('機器タイプ', max_length=50, blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)
    entry_on_progress_flag = models.IntegerField('登録中FL', blank=True, null=True)
    entry_datetime = models.DateTimeField('登録日時', blank=True, null=True)
    entry_operator = models.CharField('登録者', max_length=20, blank=True, null=True)
    update_datetime = models.DateTimeField('更新日時', blank=True, null=True)
    update_operator = models.CharField('変更者', max_length=20, blank=True, null=True)


# 詳細仕様_自由記入
class FreeSpecDetail(models.Model):
    work_id = models.IntegerField('工事id', blank=True, null=True)
    sub_no = models.IntegerField('サブNo', blank=True, null=True)
    rev_no = models.IntegerField('RevNo', blank=True, null=True)
    required_function_id = models.IntegerField('要求仕様id', blank=True, null=True)
    required_function_sub_no = models.IntegerField('要求機能サブNO', blank=True, null=True)
    entry_class = models.CharField('登録区分', max_length=20, blank=True, null=True)
    detail = models.TextField('詳細', max_length=4000, blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)
    entry_on_progress_flag = models.IntegerField('登録中FL', blank=True, null=True)
    entry_datetime = models.DateTimeField('登録日時', blank=True, null=True)
    entry_operator = models.CharField('登録者', max_length=20, blank=True, null=True)
    update_datetime = models.DateTimeField('更新日時', blank=True, null=True)
    update_operator = models.CharField('変更者', max_length=20, blank=True, null=True)


# 支給品
class Supplies(models.Model):
    work_id = models.IntegerField('工事id', blank=True, null=True)
    rev_no = models.IntegerField('RevNo', blank=True, null=True)
    supplies_name = models.CharField('支給品', max_length=50, blank=True, null=True)
    entry_class = models.CharField('登録区分', max_length=20, blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)
    entry_on_progress_flag = models.IntegerField('登録中FL', blank=True, null=True)
    entry_datetime = models.DateTimeField('登録日時', blank=True, null=True)
    entry_operator = models.CharField('登録者', max_length=20, blank=True, null=True)
    update_datetime = models.DateTimeField('更新日時', blank=True, null=True)
    update_operator = models.CharField('変更者', max_length=20, blank=True, null=True)


# 工事関係法令
class WorkLaw(models.Model):
    work_id = models.IntegerField('工事id', blank=True, null=True)
    rev_no = models.IntegerField('RevNo', blank=True, null=True)
    law_name = models.CharField('法令', max_length=50, blank=True, null=True)
    entry_class = models.CharField('登録区分', max_length=20, blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)
    entry_on_progress_flag = models.IntegerField('登録中FL', blank=True, null=True)
    entry_datetime = models.DateTimeField('登録日時', blank=True, null=True)
    entry_operator = models.CharField('登録者', max_length=20, blank=True, null=True)
    update_datetime = models.DateTimeField('更新日時', blank=True, null=True)
    update_operator = models.CharField('変更者', max_length=20, blank=True, null=True)