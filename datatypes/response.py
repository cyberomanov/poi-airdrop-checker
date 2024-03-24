from pydantic import BaseModel


class PoiData(BaseModel):
    tick: str
    tid: int
    inscriptionId: str
    address: str
    balance: float
    availableBalance: float
    transferableBalance: float
    originalBalance: float
    listing_order_floor_price: str
    order_sell: str
    claimable_balance: float
    invalid_balance: float
    current_cycle: int


class PoiResponse(BaseModel):
    code: int
    message: str
    data: PoiData
