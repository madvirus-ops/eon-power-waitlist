from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import date
from enum import Enum
from .response_schemas import *


class Data(BaseModel):
    portfolio_balance: Optional[float] = None
    assets: Optional[List[Dict[str, Any]]] = None


class BaseResponse(BaseModel):
    success: bool
    message: str
    code: int

    class Config:
        from_attributes = True


class USerid(BaseModel):
    user_id: str
    access_key: Optional[str] = None


class CreateUserRes(BaseResponse):
    data: Optional[USerid] = None


class LoginRes(BaseResponse):
    data: Optional[USerid] = None


class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    country: str


class LoginUser(BaseModel):
    email: str
    password: str
    os: str


class VerifyEmail(BaseModel):
    user_id: str
    code: str


class ResendEmail(BaseModel):
    email: str


class SendPin(BaseModel):
    user_id: str


class SetPasword(BaseModel):
    email: str
    code: str
    password: str


class ChangePassword(BaseModel):
    user_id: str
    old_password: str
    new_password: str


class Setpin(BaseModel):
    user_id: str
    pin: str


class SetNewPin(BaseModel):
    user_id: str
    code: str
    new_pin: str


class ChangePin(BaseModel):
    user_id: str
    old_pin: str
    new_pin: str


class TwoFACode(BaseModel):
    user_id: str
    code: str


class setUsername(BaseModel):
    user_id: str
    username: str


class SubmitNin(BaseModel):
    user_id: str
    submission_id: str
    document_type: str
    document_number: str
    image: str
    date_of_birth: date


class SubmitBvn(BaseModel):
    user_id: str
    bvn: str


class ServicenameEnum(str, Enum):
    security = "security"
    deposit = "deposit"
    withdrawal = "withdrawal"
    price_movement = "price_movement"
    trades = "trades"
    product_announcement = "product_announcement"


class NotificationBody(BaseModel):
    user_id: str
    service_name: ServicenameEnum
    email_enabled: Optional[bool] = None
    push_enabled: Optional[bool] = None
    sms_enabled: Optional[bool] = None


class ChannelEnum(str, Enum):
    sms = "sms"
    email = "email"
    push = "push"


class UpdateNotification(BaseModel):
    user_id: str
    service_id: str
    channel: ChannelEnum
    value: bool


class AllNotification(NotificationBody):
    id: str
    name: str

    class Config:
        from_attributes = True


class AllNotifications(BaseModel):
    success: bool
    message: str
    code: int
    data: Optional[list[AllNotification]] = None


class NotificationToken(BaseModel):
    user_id: str
    token: str


class AirtimeModel(BaseModel):
    network_id: int
    phone: str
    amount: float
    userid: str
    pin: str


class internetModel(BaseModel):
    userid: str
    phone: str
    pin: str
    network_id: int
    plan_id: str


class AddDataPlan(BaseModel):
    network_id: str
    plan_id: str
    amount: int
    plan_name: str
    telco_price: int


class AddNetwork(BaseModel):
    name: str
    airtime_to_cash_phone: str
    airtime_to_cash_percent: int


class AssetEnum(str, Enum):
    crypto = "crypto"
    fiat = "fiat"


class CreateAsset(BaseModel):
    user_id: str
    currency: str
    network: Optional[str] = None


class AddWatchlist(BaseModel):
    user_id: str
    asset_name: str
    currency: str
    network: str


class BuyAsset(BaseModel):
    user_id: str
    pin: str
    amount: float
    currency: str
    network:Optional[str] = None


class SellAsset(BaseModel):
    user_id: str
    pin: str
    volume: float
    currency: str
    network:Optional[str] = None


class SendCrypto(SellAsset):
    receiving_address: str


class Statement(BaseModel):
    user_id: str
    currency: str
    format: str
    start_date: date
    end_date: date


# Table SellAsset {
#   SellID int [pk, increment]
#   AssetID int [ref: > Asset.AssetID]
#   AmountToSell decimal(18, 8)
#   Value decimal(18, 8)
#   CreatedAt datetime
#   UpdatedAt datetime
# }


# Table P2PTrade {
#   TradeID int [pk, increment]
#   BuyerID int [ref: > User.UserID]
#   SellerID int [ref: > User.UserID]
#   AssetID int [ref: > Asset.AssetID]
#   TradeAmount decimal
#   TradePrice decimal
#   CreatedAt datetime
# }


class purchaseGiftCardModel(BaseModel):
    user_id: str
    pin: str
    productId: str
    countryCode: str
    quantity: int
    unitPrice: int


class Verifypin(BaseModel):
    user_id: str
    pin: str


class Currency(Enum):
    ngn = "ngn"
    usd = "usd"


class DisplayCurrency(BaseModel):
    user_id: str
    display_currency: Currency


class WithdrawFiat(BaseModel):
    user_id: str
    pin: str
    amount: str
    account_name: str
    account_number: str
    bank_code: str


class ValidateAccount(BaseModel):
    account_number: str
    bank_code: str


class RemoveWatclist(BaseModel):
    user_id: str
    currency: str


# class Chartinterval(str,Enum):
#     ONE_HOUR = "h1"
#     ONE_DAY = "m15"
#     ONE_WEEK = "h2"
#     ONE_MONTH = "h12"


class AppSettingsBase(BaseModel):
    app_version: Optional[str] = None
    admin_customer_id: Optional[str] = None
    maintenance_message: Optional[str] = None
    maintenance_mode: Optional[bool] = None
    promo_banner: Optional[str] = None
    promo_url: Optional[str] = None
    
    # Core services
    send_crypto: Optional[bool] = None
    buy_crypto: Optional[bool] = None
    sell_crypto: Optional[bool] = None
    can_withdraw: Optional[bool] = None
    p2p_service: Optional[bool] = None
    buy_airtime: Optional[bool] = None
    buy_data: Optional[bool] = None
    buy_giftcard: Optional[bool] = None
    
    # Fees
    selling_market: Optional[str] = None
    buying_fee: Optional[float] = None
    selling_fee: Optional[float] = None
    transfer_charge: Optional[float] = None
    exchange_rate: Optional[float] = None
    giftcard_fee: Optional[float] = None

    business_name: Optional[str] = None
    business_address: Optional[str] = None
    chat_url: Optional[str] = None
    email: Optional[str] = None
    facebook: Optional[str] = None
    instagram: Optional[str] = None
    twitter: Optional[str] = None
    phone_number: Optional[str] = None


class AdminAdressShema(BaseModel):
    btc_address: Optional[str] = None
    eth_address: Optional[str] = None
    ltc_address: Optional[str] = None
    usdt_address: Optional[str] = None
    bnb_address: Optional[str] = None
    trx_address: Optional[str] = None
    matic_address: Optional[str] = None
    xrp_address: Optional[str] = None
    doge_address: Optional[str] = None


class SaveWithdrawal(BaseModel):
    user_id: str
    bank_name: str
    bank_code: str
    account_number: str
    account_name: str