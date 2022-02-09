# -*- encoding=utf8 -*-
__author__ = "VyHN"

from airtest.core.api import *
from poco.drivers.cocosjs import CocosJsPoco

auto_setup(__file__)
poco = CocosJsPoco()

# =========================== General =========================== 

NOTIFICATION = "NOTIFICATIONS"
BTN_CLOSE = "btnClose"
BTN_OK = "btnOk"
BTN_CANCEL = "_btnNegative"
BTN_CLOSE_NOTI = "_btnClose"
TITLE_GUI = "_lbTitle"
TITLE_GUI1 = "lbTitle"
TXT_GOLD = "lbGold"
# List payment
PAYMENT = "lvPayment"
# UI nhận quà chung
CONGRATS = "congrats"
NODE_GOLD_VPOINT = "nodeGoldVPoint"
BTN_RECEIVE = "btnReceive"
BTN_BACK = "btnBack"
BTN_EXIT = "btnExit"

# =========================== Login =========================== 

BTN_GUEST = "btnGuest"
BOX_NAME = "ebLoginUsername"
BOX_PASS = "ebLoginPass"
BTN_LOGINZ = "btnLogin"
BTN_REGISTER = "btnRegister"
TXT_ACC_EXISTS = "Akun sudah ada."
TXT_ACC_INCORRECT = "Nama pengguna/Kata sandi salah,"
BTN_OUT_LOGINZ = "btnBack"

# =========================== Logout =========================== 

BTN_LOG_OUT = "btnLogout"

# =========================== Lobby =========================== 

BTN_VIP = "spineVip"
BTN_SELECT_TABLE = "btnChooseTableLarge"
BTN_PLAY = "btnQuickPlay"
NODE_AVATAR = "nodeImgAvatar"
AVATAR = "imgAvatarBorder"
BTN_SHOP = "spineShop"
BTN_MAIL = "btnMail"
BTN_RANKING = "btnRanking"
FEATURE_WC = "btnBirthday"
BTN_DEAL_WC = "btnBirthdayOffer"
FEATURE_DB = "FeatureDailyBonus"
BTN_FEATURE = "btnClick"
BTN_SETTING = "btnSetting"
BTN_TUTORIAL = "btnTut"
TXT_GOLD_LOBBY = "lbGold"

# =========================== Profile =========================== 

TXT_USER_ID = 'lbId'

# =========================== In Table ===========================

BTN_LEAVE_GAME = "btnExit"
HAND_START = "table_start"
NODE_JACKPOT = "nodeJackpot"

NODE_SCORE = "nodeScore"
TXT_TOP_POINT = "lbText0"
TXT_MIDDLE_POINT = "lbText1"
TXT_BOTTOM_POINT = "lbText2"
TXT_TOTAL_POINT = "lbTextTotal"

EFFECT_WIN = "table_winner_glow"

# =========================== Tutorial =========================== 

BTN_GO = "btnCallBack"
BTN_SKIP = "btnSkip"
IMG_HAND = "hand.png"
CONTENT = "txtContent"
TEXT_CONTENT = "Welcome to Pusoy Dos ZingPlay Let me show you how to play! ^o^"

# =========================== Support =========================== 

SUPPORT = "SOPORTE" # Text in popup Gold Support
BTN_CLAIM_SUPPORT = "btnGet"

# =========================== Daily Bonus =========================== 

TXT_DAY_BONUS = "lbDay"
TXT_TIME_REMAIN = "lbTimeRemain"
BTN_CLAIM_BONUS = "fx_btn_collect"
SLOT_DAY = "nodeDay" #imgDay1-7
IMG_TICK = "imgTick"
EFFECT_TODAY = "imgFxLight"
TXT_TODAY = "Today"

# =========================== Event WC =========================== 

TITLE_GUI = 'lbTitle'
POPUP_WC = "imgTouch"
BTN_ACTION = "btnAction"
BTN_WC_IN_TABLE = 'WCProgressTable'
PROGRESS_IN_TABLE = "lbAccumulationValue"

TITLE_WC = "WEEKLY CHALLENGE" 
NODE_DAY = "nodeDay"
TXT_DAY_MISSION = "_lbDay"
IMG_NOT_COMPLETE = "_imgEnd"
IMG_COMPLETE = "_imgTick"
TXT_TOTAL_ITEM = "lbNumOfTotalEnergies"

TXT_DAY_CHALLENGE = "lbDayChallenge"
TXT_MISSION_DETAIL = "lbMissionDetail"
TXT_PROGRESS = "lbProgress"
TXT_ITEM_REWARD = "lbItem"
TXT_GOLD_REWARD = "lbGoldReward"
BTN_ACTION = "lbAction"
ACT_PLAY_NOW = "Play Now"
ACT_CLAIM = "Claim"
TXT_THANK = "lbThankYou"

TITLE_DEAL = "SWEET DEALS" 
NODE_OFFER = "nodeOffer"
TXT_VPOINT = "lbVpoint"
TXT_BONUS = "lbBonus"
TXT_AVAILABLE = "lbAvailable"
TXT_TIME_LEFT = "lbTimeLeft"
TXT_PRICE = "lbPrice"
NODE_BOUGHT = "nodeBought"

# =========================== Popup Claim Gold =========================== 

BG_REASON = 'bgReason'
TXT_REASON = 'lbReason'
GOOD_LUCK = "Buena suerte" # Text in popup claim reward's new user
BUY_SUCCESS = "Compra existosa"
IMG_GOLD = "imgGold"
# TXT_GOLD = "lbGold"
BTN_CLAIM_REWARD = 'btnClaim'

# =========================== Ranking =========================== 

TXT_CLAIM = "lbtextClaim"
TOP_CONGRAT = "¡Muy Bien! ¡sigues asi!"
GUI_RANKING = "Power hand Ranking"
GUI_END_RANKING = "features/ranking_power/ranking_power_title"
BTN_CONFIRM = "btnConfirm"

# =========================== Offers =========================== 

GUI_OFFER_1ST = "imgTitleBanner"
BTN_BUY = "btnBuy"
BTN_SHOP_NOW = "btnShopNow"



# =========================== Shop - VIP =========================== 

GUI_SHOP = "lvShop"

# Node vị trí quyền lợi VIP
POS_VIP = ["imgSilkNone", "imgSilkBroze", "imgSilkSliver", "imgSilkGold"]
TXT_BENEFIT = "lbBenefit" # Text các quyền lợi VIP
# TXT_PRICE = "lbBtnBroze"
BTN_BUY = ["","btnBuyBroze","btnBuySilver","btnBuyGold"]

TXT_BTN_EXTEND = 'textClaim'
BTN_PARTICIPATE = "Participamos juntos"  # Text in popup Almost Extend VIP
BTN_EXTEND = "Extender" # Text in popup Extend VIP
THANK_VIP = "VIP" # Text in popup claim gold tribute VIP
BTN_OK_EXTEND = 'btnOk'

BTN_TAB_VIP = 'btnVip' # Tab VIP trong shop
BTN_OUT_VIP = 'btnClose' # Thoát GUI VIP
BTN_CLAIM = "btnClaim" # Nhận gold sau khi mua VIP

LIST_ITEMS = "listViewInteraction"
ITEMS_TYPE = "lbType"
ITEM = "btnInteraction_"
TOOLTIP = "lbToolTip"


# =========================== Cheat =========================== 

BTN_CHEAT = "btnTogleMenu"
BTN_CHEAT_GOLD = "btnCheatGold"
# BTN_CHEAT_PLAYER = "btnTogleMenu"
BTN_CHEAT_2M = "2M"
LB_GOLD = "ebCheatGold"
BTN_CHEAT_GOLD = "btnCheatGold"
BTN_CHEAT_PRIVATE = "Cheat"
BOX_GOLD = 'ebGold'
BTN_SEND_CHEAT = 'btnSendCheatPlayer'
BTN_ADD_BOT = "btnAddBot" 
TXT_TIME_SERVER = "txtServerTime"
BTN_ZACC = "Zacc"
TXT_TC_ID = "___tcId___"
BTN_CHEAT_TC = "TestCase"
TXT_POINT = "cheat point"
BTN_SEND = "Send"
BTN_ACCEPT = "btnBirthdayCheatProgress"
TXT_PROCESS = "ebBirthdayCheatProgress"
BTN_CHEAT_BR = "btnViewBirthdayEvent"