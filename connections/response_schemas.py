from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import date, datetime
from enum import Enum
from .schemas import *


class BaseResponse(BaseModel):
    success: bool
    message: str
    code: int

    class Config:
        from_attributes = True


class CreatAsstDat(BaseModel):
    asset_id: Optional[str] = None


class CreatWatchDat(BaseModel):
    watchlist_id: Optional[str] = None


class CreateAssetRes(BaseResponse):
    data: Optional[CreatAsstDat] = None


class CreateWatlistRes(BaseResponse):
    data: Optional[CreatWatchDat] = None


class AllAssets(BaseModel):
    id: str
    user_id: str
    asset_name: str
    asset_type: str  # Either "crypto" or "fiat"
    description: str
    asset_value: float
    ngn_value: float
    currency: str
    network: str
    receiving_address: str

    class Config:
        from_attributes = True


class AllAssetMid(BaseModel):
    portfolio_balance: Optional[float] = None
    assets: Optional[list[AllAssets]] = None

    class Config:
        from_attributes = True


class AllAssetsList(BaseModel):
    success: bool
    message: str
    code: int
    data: Optional[AllAssetMid] = None

    class Config:
        from_attributes = True


class OneAssetList(BaseModel):
    success: bool
    message: str
    code: int
    data: Optional[AllAssets] = None

    class Config:
        from_attributes = True


class KycMidResponse(BaseModel):
    submission_id: Optional[str] = None
    bvn_completed: Optional[bool] = None
    nin_completed: Optional[bool] = None


class KycResponse(BaseResponse):
    data: Optional[KycMidResponse] = None

    class Config:
        from_attributes = True


class AllDataPlansMid(BaseModel):
    name: str
    network_id: int
    code: str
    price: int
    telco_price: int

    class Config:
        from_attributes = True


class DataplansList(BaseResponse):
    data: Optional[list[AllDataPlansMid]] = None


class NotificationMid(BaseModel):
    notification_id: Optional[str] = None
    service_name: Optional[str] = None

    class Config:
        from_attributes = True


class NotificationRes(BaseResponse):
    data: Optional[list[NotificationMid]] = None


# class AllNotificationMid(BaseModel):
#     user_id:str
#     service_name:str
#     email_enabled:Optional[bool] = None
#     push_enabled :Optional[bool] = None
#     sms_enabled :Optional[bool] = None


# class AllNotification(BaseResponse):
#     data:Optional[list[NotificationMid]] = None


class AllWatchlist(BaseModel):
    id: str
    asset_name: str
    currency: str


class WatlistOut(BaseResponse):
    data: Optional[list[AllWatchlist]] = None


class UserOutmid(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    username: str
    email: str
    phone_number: str
    level: int
    pin: str
    country: str
    is_restricted: bool
    profile_picture: str
    email_verified: bool
    last_login: datetime

    class Config:
        from_attributes = True


class UserOut(BaseResponse):
    data: Optional[UserOutmid] = None


class QRDATA(BaseModel):
    url: Optional[str] = None
    verified: Optional[bool] = None


class TwoFactorOUt(BaseResponse):
    data: Optional[QRDATA] = None
