from pydantic import BaseModel
from enum import Enum

class GenderType(str, Enum):
    male = "Male"
    female = "Female"

class PartnerType(str, Enum):
    yes = "Yes"
    no = "No"

class DependentsType(str, Enum):
    yes = "Yes"
    no = "No"

class PhoneServiceType(str, Enum):
    yes = "Yes"
    no = "No"

class MultipleLinesType(str, Enum):
    yes = "Yes"
    no = "No"

class InternetServiceType(str, Enum):
    fiber_optic = "Fiber optic"
    dsl = "DSL"
    no = "No"

class OnlineSecurityType(str, Enum):
    yes = "Yes"
    no = "No"

class OnlineBackupType(str, Enum):
    yes = "Yes"
    no = "No"

class DeviceProtectionType(str, Enum):
    yes = "Yes"
    no = "No"

class TechSupportType(str, Enum):
    yes = "Yes"
    no = "No"

class StreamingTVType(str, Enum):
    yes = "Yes"
    no = "No"

class StreamingMoviesType(str, Enum):
    yes = "Yes"
    no = "No"

class ContractType(str, Enum):
    one_year = "One year"
    two_year = "Two year"
    monthly = "Month-to-month"

class PaperlessBillingType(str, Enum):
    yes = "Yes"
    no = "No"

class PaymentMethodType(str, Enum):
    credit_card = "Credit card (automatic)"
    bank_transfert = "Bank transfer (automatic)"
    electronic_check = "Electronic check"
    mailed_check = "Mailed check"

class Features(BaseModel):
    gender: GenderType
    SeniorCitizen: bool
    Partner: PartnerType
    Dependents: DependentsType
    tenure: int
    PhoneService: PhoneServiceType
    MultipleLines: MultipleLinesType
    InternetService: InternetServiceType
    OnlineSecurity: OnlineSecurityType
    OnlineBackup: OnlineBackupType
    DeviceProtection: DeviceProtectionType
    TechSupport: TechSupportType
    StreamingTV: StreamingTVType
    StreamingMovies: StreamingMoviesType
    Contract : ContractType
    PaperlessBilling: PaperlessBillingType
    PaymentMethod: PaymentMethodType
    MonthlyCharges: float
    TotalCharges: float

    class Config:
        use_enum_values = True
        extra = "forbid"
