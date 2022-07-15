#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
import os
#import config
import logging



from aiogram.utils.markdown import hlink
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from states.forward_mess import ForwMess

bot = Bot(token='5570461721:AAFy2ZLk3yKjN6Ej6XUFF60HdQqWwRGshxc')
dp = Dispatcher(bot, storage=MemoryStorage())
log_format='%(asctime)s - %(filename)s: - %(message)s - %(name)s'
logging.basicConfig(level='DEBUG', filename='metrics.log', format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger()

#Главное меню
firstMenuKeyboard = InlineKeyboardMarkup(row_width=2)
iikoProblemButton = InlineKeyboardButton(text='iiko', callback_data='iikoProblem')
FRButton = InlineKeyboardButton(text='Касса и Фискальный регистратор', callback_data='FRButton')
CashlessPaymentButton = InlineKeyboardButton(text='Безналичная оплата. Проблемы с оплатой заказа', callback_data='CashlessPayment')
screenButton = InlineKeyboardButton(text='Экран покупателя', callback_data='screen')
InternetButton = InlineKeyboardButton(text='Интернет', callback_data='Internet')
DeliveryButton = InlineKeyboardButton(text='Доставка', callback_data='Delivery')
ArchivingProgramButton = InlineKeyboardButton(text='Архивная программа', callback_data='ArchivingProgram')
#CCTVButton = InlineKeyboardButton(text='Видеонаблюдение', callback_data='CCTV')
ElectronicQueueAndTVButton = InlineKeyboardButton(text='Электронная очередь и ТВ', callback_data='ElectronicQueueAndTV')
#ProblemsInTheOfficeButton = InlineKeyboardButton(text='Проблемы в офисе', callback_data='ProblemsInTheOffice')
OtherButton = InlineKeyboardButton(text='Другое', callback_data='Other')
firstMenuKeyboard.add(iikoProblemButton, FRButton,CashlessPaymentButton, screenButton, InternetButton, DeliveryButton, ArchivingProgramButton,  ElectronicQueueAndTVButton, OtherButton )#, helpButton)

#Кнопки назад
backToIIKOKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToIIKOKeyboard')
backToErrorsToOrderStatusesAndProgramOperationKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToErrorsToOrderStatusesAndProgramOperationKeyboard')
backToErrorsTheOpeningAndClosingOfTheCashRegisterShiftKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToErrorsTheOpeningAndClosingOfTheCashRegisterShiftKeyboard')
backToFRButtonKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToFRButtonKeyboard')
backToProblemsPayKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToProblemsPayKeyboard')
backToCashBoxProblemsKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToCashBoxProblemsKeyboard')
backToOtherFRKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToOtherFRKeyboard')
backToscreenKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToscreenKeyboard')
backToCashlessPaymentKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToCashlessPaymentKeyboard')
backToProblemsAfterOrderPaymentKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToProblemsAfterOrderPaymentKeyboard')
backToProblemWithPaymentOrdersKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToProblemWithPaymentOrdersKeyboard')
backToProblemsPaymentForTheOrderKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToProblemsPaymentForTheOrderKeyboard')
backToInternetKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToInternetKeyboard')
backToInternetOnCashboxKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToInternetOnCashboxKeyboard')
backToOtherInternetKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToOtherInternetKeyboard')
backToDeliveryKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToDeliveryKeyboard')
backToElectronicQueueAndTVKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToElectronicQueueAndTVKeyboard')
backToMainMenuKeyboard=InlineKeyboardButton(text="Вернуться назад",callback_data='backToMainMenuKeyboard')

#Кнопки: "По IIKO"

IIKOKeyboard= InlineKeyboardMarkup (row_width=1)
ErrorsToOrderStatusesAndProgramOperationButton = InlineKeyboardButton(text='Ошибки связанные со статусами заказов и работы программы', callback_data='ErrorsToOrderStatusesAndProgramOperation')
ErrorsTheOpeningAndClosingOfTheCashRegisterShiftButton= InlineKeyboardButton(text='Ошибки связанные с открытием и закрытием кассовой смены', callback_data='ErrorsTheOpeningAndClosingOfTheCashRegisterShift')
IIKOKeyboard.add(ErrorsToOrderStatusesAndProgramOperationButton, ErrorsTheOpeningAndClosingOfTheCashRegisterShiftButton, backToMainMenuKeyboard)

ErrorsToOrderStatusesAndProgramOperationKeyboard = InlineKeyboardMarkup (row_width=1)
WhenCloseProgramDoesNotCloseButton = InlineKeyboardButton(text='При закрытии программы, она начинает висеть и не закрывается.', callback_data='WhenCloseProgramDoesNotClose')
AYellowMessageAppearedButton = InlineKeyboardButton(text='Появилось сообщение желтого цвета, в верхнем левом углу экрана в IIKO', callback_data='AYellowMessageAppeared')
TheRequiredProductIsNotInTheListButton = InlineKeyboardButton(text='Нет необходимого товара в списке/поиске при формировании актов списания и пр.', callback_data='TheRequiredProductIsNotInTheList')
TheChefInIikoSousChefDoesNotSeeOrdersButton = InlineKeyboardButton(text='Повар в iikoSousChef не видит заказов. Хотя ранее все работало.', callback_data='TheChefInIikoSousChefDoesNotSeeOrders')
ErrorsToOrderStatusesAndProgramOperationKeyboard.add(WhenCloseProgramDoesNotCloseButton, AYellowMessageAppearedButton, TheRequiredProductIsNotInTheListButton, TheChefInIikoSousChefDoesNotSeeOrdersButton, backToIIKOKeyboard)

ErrorsTheOpeningAndClosingOfTheCashRegisterShiftKeyboard = InlineKeyboardMarkup (row_width=1)
FailedToSetCashierNameButton = InlineKeyboardButton(text='При открытии кассовой смены выдает ошибку "Не удалось задать имя кассира..."', callback_data='FailedToSetCashierName')
HoursHaveExpiredYouNeedToCloseShiftButton = InlineKeyboardButton(text='При попытке оплатить заказ выдаёт ошибку "Истекли 24 часа, необходимо закрыть смену"', callback_data='HoursHaveExpiredYouNeedToCloseShift')
EmployeeCantWorkHereButton = InlineKeyboardButton(text='При попытке Авторизации пишет: «Нет ИНН», «Нет сотрудника», «Сотрудник не может тут работать»', callback_data='EmployeeCantWorkHere')
ErrorsTheOpeningAndClosingOfTheCashRegisterShiftKeyboard.add(FailedToSetCashierNameButton, HoursHaveExpiredYouNeedToCloseShiftButton, EmployeeCantWorkHereButton, backToIIKOKeyboard)


#Кнопки: "Фискальный регистратор"
FRButtonKeyboard = InlineKeyboardMarkup(row_width=1)
ProblemsPayButton = InlineKeyboardButton(text='Проблемы при попытке оплатить заказ', callback_data='ProblemsPay')
CashBoxProblemsButton = InlineKeyboardButton(text='Проблемы с кассой (после оплаты и при открытии смены)', callback_data='CashBoxProblems')
OtherFRButton = InlineKeyboardButton(text='Другое', callback_data='OtherFR')
FRButtonKeyboard.add(ProblemsPayButton, CashBoxProblemsButton, OtherFRButton, backToMainMenuKeyboard)

ProblemsPayKeyboard = InlineKeyboardMarkup(row_width=1)
NoConnectionWDeviceButton = InlineKeyboardButton(text='Нет связи с устройством', callback_data='NoConnectionWDevice')
FailedSerialNumberButton = InlineKeyboardButton(text='Не удалось получить серийный номер устройства', callback_data='FailedSerialNumber')
FNStorageButton = InlineKeyboardButton(text='Исчерпан ресурс хранения ФН', callback_data='FNStorage')
CloseShiftButton = InlineKeyboardButton(text='Истекли 24 часа, необходимо закрыть смену', callback_data='CloseShift')
FailedOperatingModeButton = InlineKeyboardButton(text='Не удалось установить режим работы (Произошла ошибка -3822)', callback_data='FailedOperatingMode')
FailedToCloseCheckButton = InlineKeyboardButton(text='Не удалось закрыть чек (Произошла ошибка -4015)', callback_data='FailedToCloseCheck')
FailedToGetPaymentMethodButton = InlineKeyboardButton(text='Не удалось получить способ оплаты', callback_data='FailedToGetPaymentMethod')
NotSupportedDeviceModeButton = InlineKeyboardButton(text='Не поддерживается в данном режиме устройства', callback_data='NotSupportedDeviceMode')
ProblemsPayKeyboard.add(NoConnectionWDeviceButton, FailedSerialNumberButton, FNStorageButton, CloseShiftButton, FailedOperatingModeButton, FailedToCloseCheckButton, FailedToGetPaymentMethodButton, NotSupportedDeviceModeButton, backToFRButtonKeyboard)

CashBoxProblemsKeyboard = InlineKeyboardMarkup(row_width=1)
FailedToSetNameButton = InlineKeyboardButton(text='При открытии кассовой смены выдает ошибку ,,Не удалось задать имя кассира...,,', callback_data='FailedToSetName')
NoConnectionToOFDButton = InlineKeyboardButton(text='После оплаты на кассе всплывает уведомление ,, Нет связи с ОФД. Колличество неотправленных докуметов: 1', callback_data='NoConnectionToOFD')
ErrorChequeButton = InlineKeyboardButton(text='После оплаты на кассе всплывает уведомление ,, При печати фискального чека произошла ошибка (-3807) ,,', callback_data='ErrorCheque')
CashBoxProblemsKeyboard.add(FailedToSetNameButton, NoConnectionToOFDButton, ErrorChequeButton, backToFRButtonKeyboard)

OtherFRKeyboard = InlineKeyboardMarkup(row_width=1)
JammedCarvingKnifeButton = InlineKeyboardButton(text='Заклинил нож авторезчика', callback_data='JammedCarvingKnife')
JammedCarvingKnifeSecondButton = InlineKeyboardButton(text='Заклинил нож авторезчика', callback_data='JammedCarvingKnifeSecond')
DisableAutoCutterButton = InlineKeyboardButton(text='Отключить авторезчик', callback_data='DisableAutoCutter')
OtherFRKeyboard.add(JammedCarvingKnifeButton, JammedCarvingKnifeSecondButton, DisableAutoCutterButton, backToFRButtonKeyboard)


#Экран покупателя
screenKeyboard = InlineKeyboardMarkup(row_width=1)
NoPicturesBlackScreenButton = InlineKeyboardButton(text='Нет картинок. Черный экран', callback_data='NoPicturesBlackScreen')
NoPicturesWhiteScreenButton = InlineKeyboardButton(text='Нет картинок. Белый экран', callback_data='NoPicturesWhiteScreen')
ErrorOnTheScreenBuyerButton = InlineKeyboardButton(text='На экране покупателя ошибка «Нет сигнала»', callback_data='ErrorOnTheScreenBuyer')
screenKeyboard.add(NoPicturesBlackScreenButton, NoPicturesWhiteScreenButton, ErrorOnTheScreenBuyerButton, backToMainMenuKeyboard )

#Безнал оплата

CashlessPaymentKeyboard = InlineKeyboardMarkup(row_width=1)
ProblemWithPaymentOrdersButton = InlineKeyboardButton(text='Проблема с оплатой заказов', callback_data='ProblemWithPaymentOrders')
ProblemsAfterOrderPaymentButton = InlineKeyboardButton(text='Проблемы возникшие после оплаты заказа', callback_data='ProblemsAfterOrderPayment')
ProblemsPaymentForTheOrderButton = InlineKeyboardButton(text='Проблемы связанные с безналичной оплатой заказа', callback_data='ProblemsPaymentForTheOrder')
CashlessPaymentKeyboard.add(ProblemWithPaymentOrdersButton, ProblemsAfterOrderPaymentButton, ProblemsPaymentForTheOrderButton, backToMainMenuKeyboard)

#Проблема с оплатой заказов

ProblemWithPaymentOrdersKeyboard = InlineKeyboardMarkup(row_width=1)
NoCommunicationWithDeviceButton = InlineKeyboardButton(text='"Нет связи с устройством"', callback_data='NoCommunicationWithDevice')
FailedToGetDeviceSerialNumberButton = InlineKeyboardButton(text='"Не удалось получить серийный номер устройства"', callback_data='FailedToGetDeviceSerialNumber')
FNStorageResourceExhaustedButton = InlineKeyboardButton(text='"Исчерпан ресурс хранения ФН"', callback_data='FNStorageResourceExhausted')
FailedToSetOperatingModeButton = InlineKeyboardButton(text='"Не удалось установить режим работы (Произошла ошибка -3822)"', callback_data='FailedToSetOperatingMode')
FailedToCloseCheckButton = InlineKeyboardButton(text='"Не удалось закрыть чек (Произошла ошибка -4015)"', callback_data='FailedToCloseCheck')
FailedToGetPaymentMethodButton = InlineKeyboardButton(text='"Не удалось получить способ оплаты"', callback_data='FailedToGetPaymentMethod')
NotSupportedInThisDeviceModeButton = InlineKeyboardButton(text='"Не поддерживается в данном режиме устройства"', callback_data='NotSupportedInThisDeviceMode')
WPayingForTheOrderPrepaymentWindowAppearsButton = InlineKeyboardButton(text='При оплате заказа появляется окно предоплаты"', callback_data='WPayingForTheOrderPrepaymentWindowAppears')
ProblemWithPaymentOrdersKeyboard.add(NoCommunicationWithDeviceButton, FailedToGetDeviceSerialNumberButton, FNStorageResourceExhaustedButton, FailedToSetOperatingModeButton, FailedToCloseCheckButton, FailedToGetPaymentMethodButton, NotSupportedInThisDeviceModeButton, WPayingForTheOrderPrepaymentWindowAppearsButton, backToCashBoxProblemsKeyboard )

#Проблемы возникшие после оплаты заказа

ProblemsAfterOrderPaymentKeyboard = InlineKeyboardMarkup(row_width=1)
NoConnectionToOFDNumberOfUnsentDocumentsButton = InlineKeyboardButton(text='После оплаты на кассе всплывает уведомление "Нет связи с ОФД. Колличество неотправленных докуметов: 1"', callback_data='NoConnectionToOFDNumberOfUnsentDocuments')
AnErrorOccurredWhilePrintingTheReceiptButton = InlineKeyboardButton(text='После оплаты на кассе всплывает уведомление "При печати фискального чека произошла ошибка (-3807)"', callback_data='AnErrorOccurredWhilePrintingTheReceipt')
ProblemsAfterOrderPaymentKeyboard.add(NoConnectionToOFDNumberOfUnsentDocumentsButton, AnErrorOccurredWhilePrintingTheReceiptButton, backToCashBoxProblemsKeyboard)

#Проблемы связанные с безналичной оплатой заказа
ProblemsPaymentForTheOrderKeyboard = InlineKeyboardMarkup(row_width=1)
PaymentTypeBankCardDoesNotWorkButton = InlineKeyboardButton(text='Не работает тип оплаты "Банковская карта"', callback_data='PaymentTypeBankCardDoesNotWork')
BankTerminalNotWorkingBlackScreenButton = InlineKeyboardButton(text='Не работает банковский терминал, черный экран', callback_data='BankTerminalNotWorkingBlackScreen')
ThereIsNoBankCardPaymentButton = InlineKeyboardButton(text='Нет кнопки оплаты "Баковская карта""', callback_data='ThereIsNoBankCardPayment')
ProblemsPaymentForTheOrderKeyboard.add(PaymentTypeBankCardDoesNotWorkButton, BankTerminalNotWorkingBlackScreenButton, ThereIsNoBankCardPaymentButton, backToCashBoxProblemsKeyboard)

#Кнопки по интернету

InternetKeyboard = InlineKeyboardMarkup(row_width=1)
InternetOnCashboxButton = InlineKeyboardButton(text='Интернет на кассе', callback_data='InternetOnCashbox')
WIFIButton = InlineKeyboardButton(text='Wi-Fi', callback_data='WIFI')
OtherInternetButton=InlineKeyboardButton(text='Другое', callback_data='OtherInternet')
InternetKeyboard.add(InternetOnCashboxButton, WIFIButton, OtherInternetButton, backToMainMenuKeyboard)

InternetOnCashboxKeyboard = InlineKeyboardMarkup(row_width=1)
NoConnectionsAvailableButton = InlineKeyboardButton(text='Нет доступных подключений', callback_data='NoConnectionsAvailable')
WithoutInternetAccessButton = InlineKeyboardButton(text='Без доступа к Интернету', callback_data='WithoutInternetAccess')
InternetOnCashboxKeyboard.add(NoConnectionsAvailableButton, WithoutInternetAccessButton, backToInternetKeyboard)

OtherInternetKeyboard = InlineKeyboardMarkup(row_width=1)
YellowTriangleButton = InlineKeyboardButton(text='Желтый треугольник', callback_data='YellowTriangle')
RedCrossButton = InlineKeyboardButton(text='Красный крестик, сетевой кабель не подключен', callback_data='RedCross')
InternetConnectionStatusButton = InlineKeyboardButton(text='Статус интернет соединения', callback_data='InternetConnectionStatus')
OtherInternetKeyboard.add(YellowTriangleButton, RedCrossButton, InternetConnectionStatusButton, backToInternetKeyboard)


#Кнопки: "По доставке"
DeliveryKeyboard = InlineKeyboardMarkup(row_width=1)
NoPermissionToSellButton=InlineKeyboardButton(text='У продукта ... нет разрешения продаваться в выбраной ценовой категории', callback_data='NoPermissionToSell')
DisabledOnPointButton=InlineKeyboardButton(text='Тип оплаты ... отключен на точке', callback_data='DisabledOnPoint')
CannotBeTransferredButton=InlineKeyboardButton(text='Продукт ... не может быть передан в IIIKO', callback_data='CannotBeTransferred')
PointOfSaleNotSyncedButton=InlineKeyboardButton(text='Не синхронизирована торговая точка IIKO программой доставки', callback_data='PointOfSaleNotSynced')
RequestErrorInIIKOButton=InlineKeyboardButton(text='Ошибка запроса в IIKO (не передаются заказы)', callback_data='RequestErrorInIIKO')
TheRequiredPaymentTypeButton = InlineKeyboardButton(text='Нужного типа оплаты нет в IIKO', callback_data='TheRequiredPaymentType')
DeliveryKeyboard.add(NoPermissionToSellButton, DisabledOnPointButton, CannotBeTransferredButton, PointOfSaleNotSyncedButton, RequestErrorInIIKOButton, TheRequiredPaymentTypeButton, backToMainMenuKeyboard)

#Кнопки: "По Электронной очереди"
ElectronicQueueAndTVKeyboard = InlineKeyboardMarkup(row_width=1)
ServerUnavailableMessageButton=InlineKeyboardButton(text='Касса недоступна', callback_data='ServerUnavailableMessage')
SettingUpAnElectronicQueueButton=InlineKeyboardButton(text='Настройка электронной очереди при открытии новой точки или при замене телевизора', callback_data='SettingUpAnElectronicQueue')
InternetConnectionNotWorkingOnTVButton=InlineKeyboardButton(text='На телевизоре не работает интернет соединение', callback_data='InternetConnectionNotWorkingOnTV')
ElectronicQueueAndTVKeyboard.add(ServerUnavailableMessageButton, SettingUpAnElectronicQueueButton, InternetConnectionNotWorkingOnTVButton, backToMainMenuKeyboard)




#Блок проблем в офисе

# ProblemsInTheOfficeKeyboard=InlineKeyboardMarkup(row_width=1)
# RemoteNotWorkingButton=InlineKeyboardButton(text='Не работает удаленка', callback_data='RemoteNotWorking')
# MailProblemButton=InlineKeyboardButton(text='Проблема с почтой', callback_data='MailProblem')
# NoAccessToRMSButton=InlineKeyboardButton(text='Нет доступа к РМС', callback_data='NoAccessToRMS')
# ChainProblemButton=InlineKeyboardButton(text='Проблема с чейном', callback_data='ChainProblem')
# ThePrinterIsNotWorkingButton=InlineKeyboardButton(text='Принтер не работает или есть ошибка в работе принтера', callback_data='ThePrinterIsNotWorking')
# TheScannerDoesNotWorkButton=InlineKeyboardButton(text='Сканер не работает или есть ошибка в работе принтера', callback_data='TheScannerDoesNotWork')
# ProblemsInTheOfficeKeyboard.add(RemoteNotWorkingButton, MailProblemButton, NoAccessToRMSButton,  ChainProblemButton, ThePrinterIsNotWorkingButton, TheScannerDoesNotWorkButton)

# NoAccessToRMSKeyboard = InlineKeyboardMarkup(row_width=1)
# LicenseRestrictionButton=InlineKeyboardButton(text='Лиценционное ограничение: невозможно получить подключение', callback_data='LicenseRestriction')
# NoAccessToTheServerButton=InlineKeyboardButton(text='Адрес сервера горит серым и ошибка "нет доступа к серверу"', callback_data='NoAccessToTheServer')
# NoAccessToRMSKeyboard.add(LicenseRestrictionButton, NoAccessToTheServerButton)
#
# ChainProblemKeyboard = InlineKeyboardMarkup(row_width=1)
# NoAccessToTheServerChainButton=InlineKeyboardButton(text='Адрес сервера горит серым и ошибка "нет доступа к серверу"', callback_data='NoAccessToTheServerChain')
# ServerIsNotAnIIKO_RMSButton=InlineKeyboardButton(text='Адрес сервера горит желтым и ошибка "указаный сервер не является сервером IIKO_RMS"', callback_data='ServerIsNotAnIIKO_RMS')
# ChainProblemKeyboard.add(NoAccessToTheServerChainButton, ServerIsNotAnIIKO_RMSButton)
#
# ThePrinterIsNotWorkingKeyboard = InlineKeyboardMarkup(row_width=1)
# TheRedLightIsOnButton=InlineKeyboardButton(text='Горит красная лампочка', callback_data='TheRedLightIsOn')
# CartridgeReplacementButton= InlineKeyboardButton(text='Замена картриджа', callback_data='CartridgeReplacement')
# PaperJamButton=InlineKeyboardButton(text='Замятие бумаги', callback_data='PaperJam')
# DoesntPickUpPaperButton=InlineKeyboardButton(text='Не захватывает бумагу', callback_data='DoesntPickUpPaper')
# ThePrinterIsNotWorkingKeyboard.add(TheRedLightIsOnButton, CartridgeReplacementButton, PaperJamButton, DoesntPickUpPaperButton)


callTechSuppKeyboard=InlineKeyboardMarkup(row_width=1)
callTechSuppButton=InlineKeyboardButton(text="Связаться с техподдержкой",callback_data='callTechSupp') #url='https://t.me/+wGeFnHb6ACBkOWFi',parse_mode='Markdown', disable_web_page_preview=True, callback_data='callTechSupp')
backToMainMenuButton=InlineKeyboardButton(text="Вернуться на главное меню",callback_data='backToMainMenu')
callTechSuppKeyboard.add(callTechSuppButton, backToMainMenuButton)#, helpButton)





@dp.message_handler(commands='start')
async def firstButton(message: types.Message):
    await message.answer('Здравствуйте!\n'
                         'Какие у вас появились вопросы?\n'
                        'Выберите интересующий раздел, нажав на кнопку.', reply_markup=firstMenuKeyboard)

#Блок iiko--

@dp.callback_query_handler(text='iikoProblem')
async def iikoProblem(calliiProb: types.CallbackQuery):
    await calliiProb.message.edit_text('Выберите раздел проблемы', reply_markup=IIKOKeyboard)
    logger.debug('Пользователь нажал кнопку "Вход в кабинет партнера"')

@dp.callback_query_handler(text='ErrorsToOrderStatusesAndProgramOperation')
async def ErrorsToOrderStatusesAndProgramOperation(callETOSAPO: types.CallbackQuery):
    await callETOSAPO.message.edit_text(text='Ошибки связанные со статусами заказов и работы программы:', reply_markup = ErrorsToOrderStatusesAndProgramOperationKeyboard, )
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')

@dp.callback_query_handler(text='ErrorsTheOpeningAndClosingOfTheCashRegisterShift')
async def ErrorsTheOpeningAndClosingOfTheCashRegisterShift(callETOACOTCRS: types.CallbackQuery):
    await callETOACOTCRS.message.edit_text(text='Ошибки связанные с открытием и закрытием кассовой смены:', reply_markup = ErrorsTheOpeningAndClosingOfTheCashRegisterShiftKeyboard)
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')

@dp.callback_query_handler(text='WhenCloseProgramDoesNotClose')
async def WhenCloseProgramDoesNotClose(callWCPDNC: types.CallbackQuery):
    await callWCPDNC.message.edit_text('Перезагрузите компьютер.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Чужие данные"')

@dp.callback_query_handler(text='AYellowMessageAppeared')
async def AYellowMessageAppeared(callAYMA: types.CallbackQuery):
    await callAYMA.message.edit_text(text='Закрываем на крестик, не обращаем внимания на это событие.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Другой код"')

@dp.callback_query_handler(text='TheRequiredProductIsNotInTheList')
async def TheRequiredProductIsNotInTheList(callTRPINITL: types.CallbackQuery):
    await callTRPINITL.message.edit_text(text='Необходимо проверить включены ли фильтры, позволяющие осуществить поиск, а именно: «Вся номенкл.» а также поиск по «Артикул» и «Код» должны быть выделены жёлтым цветом[.](https://downloader.disk.yandex.ru/preview/3cba7e3ff09569e3be52e80672e4ac6c97426f075a6f27a63332af8942c6a2e0/62a9d873/d0i8uuZ70gOS25grgQS1L3tULxkGzTinepbZrG0mpwnlTSftT-A5760nIzFfbN9OvgN3zLH-m_bKBZxpj24wnw%3D%3D?uid=0&filename=%D0%92%D0%BE%D0%BF%D1%80%D0%BE%D1%81%205.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=958x912)', parse_mode='Markdown', disable_web_page_preview=False, reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Аккаунт партнера"')

@dp.callback_query_handler(text='TheChefInIikoSousChefDoesNotSeeOrders')
async def TheChefInIikoSousChefDoesNotSeeOrders(callTCIISCDNSO: types.CallbackQuery):
    await callTCIISCDNSO.message.edit_text(text='1)На экране повара необходимо зайти в настройки.\n'
                                                 '2)Включить все статусы для отображения:\n'
                                                 'Ожидает\n'
                                                 'Готовится\n'
                                                 'Приготовлено\n'
                                                 'Подано[.](https://downloader.disk.yandex.ru/preview/4efb3509be203a5c0f88c304df1d4f52705ef55c0c192ae662768bf98ca7d58d/62a9d873/hAgBFsYa986PT0j0AELyP3tULxkGzTinepbZrG0mpwl8zdN8fP0mrPrjfgUBqamZ0Xlyqrs9heLpT1euRuLiqQ%3D%3D?uid=0&filename=%D0%92%D0%BE%D0%BF%D1%80%D0%BE%D1%81%206.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=958x912)\n'
                                                 '3) Если данное решение не помогло, необходимо обратиться в техническую поддержку', parse_mode='Markdown', disable_web_page_preview=False, reply_markup=callTechSuppKeyboard)

    logger.debug('Пользователь нажал кнопку "Аккаунт партнера"')

@dp.callback_query_handler(text='FailedToSetCashierName')
async def FailedToSetCashierName(callFTSCN: types.CallbackQuery):
    await callFTSCN.message.edit_text(text='Связаться с техподдержкой', reply_markup = callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')

@dp.callback_query_handler(text='HoursHaveExpiredYouNeedToCloseShift')
async def HoursHaveExpiredYouNeedToCloseShift(callHHEYNTCS: types.CallbackQuery):
    await callHHEYNTCS.message.edit_text(text='Вчера сотрудники забыли закрыть кассовую смену.\n'
                                           'Закрываем кассовую смену через iiko.\n'
                                           'Текущий заказ можно удалить и пробить в актуальной смене.', reply_markup = callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')

@dp.callback_query_handler(text='EmployeeCantWorkHere')
async def EmployeeCantWorkHere(callECWH: types.CallbackQuery):
    await callECWH.message.edit_text(text='По каждому из вопросов кассиру необходимо обратиться в Отдел кадров.', reply_markup = callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')

#Экран покупателя
@dp.callback_query_handler(text='screen')
async def screen(callscreen: types.CallbackQuery):
    await callscreen.message.edit_text(text='Какая у вас ошибка?:', reply_markup = screenKeyboard)
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')

@dp.callback_query_handler(text='NoPicturesBlackScreen')
async def NoPicturesBlackScreen(callNPBS: types.CallbackQuery):
    await callNPBS.message.edit_text(text='1.Выключите и включите экран покупателя, убедитесь, что запущена программа iiko.\n'
                                       '2.Выйдите на рабочий стол и правой кнопкой мыши нажмите на любое свободное место, выберите «Параметры экрана»\n'
                                       '3.В открывшемся окне нужно найти пункт «Несколько дисплеев» и в нем выбрать «Расширить эти экраны» и сохранить\n'
                                       '4.Если эти действия не помогли или в предыдущем пункте не отображается второй экран обратитесь в техподдержку[.](https://downloader.disk.yandex.ru/preview/521a83d844e5db61a5f6c34082e6eb3bd5abc516018ccc03b478edb535ee00c8/62ae01db/8YutTHL1-KXXXyNdsGXSi7dFe3lZhuIBDAkrsa9RokqBOT3otlxb4L0ZY9vRyZNgwayUiwbHeDO8hfh4byqR8Q%3D%3D?uid=0&filename=%D1%87%D0%B5%D1%80%D0%BD%D1%8B%D0%B9%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup = callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')

@dp.callback_query_handler(text='NoPicturesWhiteScreen')
async def NoPicturesWhiteScreen(callNPWS: types.CallbackQuery):
    await callNPWS.message.edit_text(text='Перезагрузите компьютер. Если проблема сохранилась, необходимо, чтобы Ваш управляющий обратился в отдел маркетинга к Никитенко Анастасии.', reply_markup = callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')

@dp.callback_query_handler(text='ErrorOnTheScreenBuyer')
async def ErrorOnTheScreenBuyer(callEOTSB: types.CallbackQuery):
    await callEOTSB.message.edit_text(text='1.Выключите компьютер. Сзади на экране покупателя отключите и подключите оба кабеля.\n'
                                        '2.Если у вас компьютер новой модели, как на картинке, то необходимо на экране покупателя найти кнопки. Выключите и включите экран, нажмите кнопку SELECT и, в появившемся меню, с помощью кнопок «+» или «-» выберите пункт DP (Display Port) и еще раз нажмите SELECT.\n'
                                        '3.Перезагрузите компьютер, включите iiko. Если после полной загрузки изображения так и не появились обратитесь в техподдержку[.](https://downloader.disk.yandex.ru/preview/dd319708affe1134d100ee43732c87538ae6439cb0d5ebbb6aa35dc1b0976790/62ae02ad/knlohDtvQKYMq_MhqyNUHFPSm-SVx5vLBpTPrbcn0geiQ2TsaOjakpfe6ywj_gpQOxYUtZgGGuNW9NiMJ0xFvg%3D%3D?uid=0&filename=noSig.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)', parse_mode='Markdown', reply_markup = callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Частые проблемы"')


#Архивная программа

@dp.callback_query_handler(text='ArchivingProgram')
async def ArchivingProgram(callAProgram: types.CallbackQuery):
    await callAProgram.message.edit_text(text='Если на торговой точке нет панели, где вы отправляете накладные в офис, то необходимо на рабочем столе найти ярлык SAdminClient\n'
                                               'Если ярлыка нет, то нужно перейти по пути C:\SAdminClient\ и запустить файл SAClientDesktop.exe[.](https://downloader.disk.yandex.ru/preview/7c19849c54747195e4b32923e24b436833caa7fc39ab8b474a888a2f40a39e1d/62a9e929/C24lWJcR8Z0Wpl6RSD-WRd02Ahv8dYkEorV1KGwzBbNRhWzWrZoC0Xc6damtB37t95QRKAGuNuXwpz0e4Wwalg%3D%3D?uid=0&filename=%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%20%D0%B4%D0%BB%D1%8F%20%D1%87%D0%B0%D1%82%D0%B0%D0%A2%D0%9F.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)\n'
                                               'По всем остальным вопросам необходимо обратиться в техподдержку', parse_mode='Markdown', disable_web_page_preview=False, reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Ссылки"')

#Блок по Электронной очереди и телеку
@dp.callback_query_handler(text='ElectronicQueueAndTV')
async def ElectronicQueueAndTV(callElQATV: types.CallbackQuery):
    await callElQATV.message.edit_text(text='Какая ошибка:', reply_markup=ElectronicQueueAndTVKeyboard)

@dp.callback_query_handler(text='ServerUnavailableMessage')
async def ServerUnavailableMessage(callSULM: types.CallbackQuery):
    await callSULM.message.edit_text(text='Чтобы возобновить работу системы электронной очереди, необходимо:\n'
                                          '\n'
                                          'Вариант 1:\n'
                                          'Перезагрузите компьютер (чаще всего после этого проблема устраняется)\n'
                                          '\n'
                                          'Вариант 2:\n'
                                          '1) Проверьте запущен ли на компьютере IikoFront\n'
                                          '2) Если он запущен, но ошибка все так же отображается, то необходимо перезапустить IikoFront (выйти из IikoFront и снова зайти)\n'
                                          '\n'
                                          'Вариант 3:\n'
                                          'Проверьте есть ли на телевизоре интернет соединение:\n'
                                          '1) Откройте новую вкладку в браузере на телевизоре и попробуйте что-нибудь найти в поисковой строке\n'
                                          '2) Если никакой сайт не открывается, то дело в интернет соединении на телевизоре и далее есть два варианта:\n'
                                          'a) Если интернет подключен к телевизору через кабель, то проверьте что кабель плотно воткнут в телевизор и в роутер. Переподключите кабель.'
                                          'b) Если интернет подключен к телевизору через Wi-Fi, то перезагрузите роутер (вытащив его из розетки и снова подключив). В настройках телевизора выбрать необходимую сеть.\n'
                                          '\n'
                                          'Вариант 4:\n'
                                          '1) Откройте браузер на телевизоре, где отображается элетронная очередь;\n'
                                          '2) Введите в адресную строку в новой вкладке: http://192.168.1.101:3100/ или http://localhost:3100/\n'                                   
                                          '3. Готово! На экране должна появиться электронная очередь (см. на изображении ниже). Если она появилась, то система работает корректно\n'
                                          'Далее переходите к настройке работы электронной очереди на телевизоре, размещенном на торговой точке[.](https://downloader.disk.yandex.ru/preview/5b9dd25f8256790edec75bf813452ada181acd8cad826dfce54728b405708917/62adcb39/rzQ7cVpmbwGlKJ3Jf2lrzToeSj49mKz4OXPeLrwbFnBu0bMCeBAcDwTqpPbSTlWcnKbhSwZGFJLxDlllgFNReg%3D%3D?uid=0&filename=%D0%BE%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)', parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Ссылки"')

@dp.callback_query_handler(text='SettingUpAnElectronicQueue')
async def SettingUpAnElectronicQueue(callSUAEQ):
    document=open('pic/Инструкция_по_настройке_электронной_очереди_на_телевизоре.pdf', 'rb')
    await callSUAEQ.message.answer_document(document)



    logger.debug('Пользователь нажал кнопку "Ссылки"')

@dp.callback_query_handler(text='InternetConnectionNotWorkingOnTV')
async def InternetConnectionNotWorkingOnTV(callICNWOT: types.CallbackQuery):
    await callICNWOT.message.edit_text(text='a) Если интернет подключен к телевизору через кабель, то провереьте что кабель плотно воткнут в телевизор и в роутер. Переподключите кабель.\n'
                                         'б) Если интернет подключен к телевизору через Wi-Fi, то перезагрузите роутер (вытащив его из розетки и снова подключив). В настройках телевизора выбрать необходимую сеть.', parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Ссылки"')

#Блок видеонаблюдения

@dp.callback_query_handler(text='CCTV')
async def CCTV(callCCTV: types.CallbackQuery):
    await callCCTV.message.edit_text(text='Для того, чтобы заявка была взята в работу, необходимо поставить задачу в битрикс на Старцева Андрея https://sushimarke.bitrix24.ru/', parse_mode='Markdown', disable_web_page_preview=True, reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Ссылки"')


#Блок Фискальный Регистратор
@dp.callback_query_handler(text='FRButton')
async def FRButton(callsFRButton: types.CallbackQuery):
    await callsFRButton.message.edit_text(text='Проблемы с фискальным регистратором', reply_markup=FRButtonKeyboard)


@dp.callback_query_handler(text='ProblemsPay')
async def ProblemsPay(callsPP: types.CallbackQuery):
    await callsPP.message.edit_text(text='Проблемы при попытке оплатить заказ', reply_markup=ProblemsPayKeyboard)

@dp.callback_query_handler(text='CashBoxProblems')
async def CashBoxProblems(callsCBP: types.CallbackQuery):
    await callsCBP.message.edit_text(text='Проблемы с кассой', reply_markup=CashBoxProblemsKeyboard)

@dp.callback_query_handler(text='OtherFR')
async def OtherFR(callOFR: types.CallbackQuery):
    await callOFR.message.edit_text(text='Какая проблема:', reply_markup=OtherFRKeyboard)

@dp.callback_query_handler(text='JammedCarvingKnife')
async def JammedCarvingKnife(callJCK: types.CallbackQuery):
    await callJCK.message.edit_text(text='Заклинил нож авторезчика[.](https://downloader.disk.yandex.ru/preview/35b1eb5205679498ff3b17a4045e10993adcfed08570a8d40be20ac275912e17/62acf0ad/ESxb9eO2_yOmY-D99Xdd3HKLjK3Tbuf5Fe8yWan6E55P8ljA1o_gTN5cwHdckOW_la0JuxGYXGpXwJ1Gjlqm4g%3D%3D?uid=0&filename=%D0%97%D0%B0%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BB%20%D0%BD%D0%BE%D0%B6%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BE%D1%82%D1%80%D0%B5%D0%B7%D1%87%D0%B8%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)

@dp.callback_query_handler(text='JammedCarvingKnifeSecond')
async def JammedCarvingKnifeSecond(callJCKS: types.CallbackQuery):
    await callJCKS.message.edit_text(text='Заклинил нож авторезчика 2[.](https://downloader.disk.yandex.ru/preview/27cd4ed31021d6ec6f78f285da16416084e24759caa08f5c2006122be00632a3/62acf0d7/h6mfhyaWonI9UKVtlgtmTHKLjK3Tbuf5Fe8yWan6E56mzpxop76MmjFidzZxWDuWwK7184_0ojAfzYPGu2ckvw%3D%3D?uid=0&filename=%D0%97%D0%B0%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BB%20%D0%BD%D0%BE%D0%B6%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BE%D1%82%D1%80%D0%B5%D0%B7%D1%87%D0%B8%D0%BA%D0%B0%202.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)

@dp.callback_query_handler(text='DisableAutoCutter')
async def DisableAutoCutter(callDAC: types.CallbackQuery):
    await callDAC.message.edit_text(text='Отключить авторезчик[.](https://downloader.disk.yandex.ru/preview/519e9afcff0eec82b397610517f74d87952c45fe39dc33ca020ae345f44a415d/62acf0f0/q4tF9qL4jasrDr9GpYO620Nr5e5Udatibtj0bReQGm6EYDJgGEQeRyUpeQa3gdxcsVgPMTKA-j4bjIs8NBhKlA%3D%3D?uid=0&filename=%D0%9E%D1%82%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BE%D1%82%D1%80%D0%B5%D0%B7%D1%87%D0%B8%D0%BA.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)

#Блок проблем при попытке оплатить заказ
@dp.callback_query_handler(text='NoConnectionWDevice')
async def NoConnectionWDevice(callsNCWD: types.CallbackQuery):
    await callsNCWD.message.edit_text(text='Проверить, включен ли фискальный регистратор, так-же проверить качество подключения проводов к нему (питание+ЮСБ провода).\n'
                                            'Так-же проверить подключение ЮСБ провода со стороны компьютера.\n'
                                            'Если вышеперечисленные действия не помогли - обратиться в техподдержку.', reply_markup=callTechSuppKeyboard)

@dp.callback_query_handler(text='FNStorage')
async def FNStorage(callaFNStorage: types.CallbackQuery):
    await callaFNStorage.message.edit_text(text='Необходимо обратиться в техническую поддержку.',reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "После отправки заявки"')

@dp.callback_query_handler(text='FailedSerialNumber')
async def FailedSerialNumber(callsFSN: types.CallbackQuery):
    await callsFSN.message.edit_text(text='Выключить фискальный регистратор на кнопку и включить заново.\n'
                                             'Завершить процесс IIKO через диспетчер задач, запустить IIKO заново и повторить оплату.\n'
                                             'Если вышеперечисленные действия не помогли - обратиться в техподдержку.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Статусы заявок"')

@dp.callback_query_handler(text='CloseShift')
async def CloseShift(callsCShift: types.CallbackQuery):
    await callsCShift.message.edit_text(text='Вчера сотрудники забыли закрыть кассовую смену.\n'
                                           'Закрываем кассовую смену через iiko.\n'
                                            'Текущий заказ можно удалить и пробить в актуальной смене.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Статус: Не подлежит вознаграждению"')

@dp.callback_query_handler(text='FailedOperatingMode')
async def FailedOperatingMode(callFOM: types.CallbackQuery):
    await callFOM.message.edit_text(text='Вчера сотрудники забыли закрыть кассовую смену. \n'
                                         'Закрываем кассовую смену через iiko. Текущий заказ можно удалить и пробить в актуальной смене.', reply_markup=callTechSuppKeyboard)

@dp.callback_query_handler(text='FailedToCloseCheck')
async def FailedToCloseCheck(callFTC: types.CallbackQuery):
    await callFTC.message.edit_text(text='Необходимо обратиться в техническую поддержку.', reply_markup=callTechSuppKeyboard)

@dp.callback_query_handler(text='FailedToGetPaymentMethod')
async def FailedToGetPaymentMethod(callFTGM: types.CallbackQuery):
    await callFTGM.message.edit_text(text='Необходимо обратиться в техническую поддержку.', reply_markup=callTechSuppKeyboard)

@dp.callback_query_handler(text='NotSupportedDeviceMode')
async def NotSupportedDeviceMode(callNSDM: types.CallbackQuery):
    await callNSDM.message.edit_text(text='Необходимо выключить и включить фискальный регистратор и перезагрузить программу IIKO.\n'
                                           'Если вышеперечисленные действия не помогли - обратиться в техподдержку.', reply_markup=callTechSuppKeyboard)

#Блок проблем с кассой (после оплаты и при открытии смены)

@dp.callback_query_handler(text='FailedToSetName')
async def FailedToSetName(callFTSN: types.CallbackQuery):
    await callFTSN.message.edit_text(text='Необходимо обратиться в техническую поддержку.', reply_markup=callTechSuppKeyboard)

@dp.callback_query_handler(text='NoConnectionToOFD')
async def NoConnectionToOFD(callNCTOFD: types.CallbackQuery):
    await callNCTOFD.message.edit_text(text='Такое уведомление ВСЕГДА появляется после каждого закрытого заказа\n'
                                           ' Если в данном уведомлении количество документов больше, чем ,,1,, необходимо обратиться в техническую поддержку.', reply_markup=callTechSuppKeyboard)

@dp.callback_query_handler(text='ErrorCheque')
async def ErrorCheque(callEC: types.CallbackQuery):
    await callEC.message.edit_text(text='Данная ошибка говорит о том, что фискальный регистратор не видет чековую ленту, либо она отстутсвует.\n'
                                           'Если ошибка возникла при замене рулона на новый, откройте крышку фискальника и отмотайте с рулона небольшое количество ленты.\n'
                                           'Далее закройте крышку и повторите оплату заказа.', reply_markup=callTechSuppKeyboard)


#Блок Интернет
@dp.callback_query_handler(text='Internet')
async def Internet(callInternet: types.CallbackQuery):
    await callInternet.message.edit_text(text='Проблемы с интернетом',reply_markup=InternetKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='WIFI')
async def WIFI(callWIFI: types.CallbackQuery):
    await callWIFI.message.edit_text(text='Ваш Wi-Fi должен называться Sushi-market или Lavash, пароль s240203S. \n'
                                           'Если нет сети или не подходит пароль, то необходимо обратиться в техническую поддержку по номеру +7 965 979 0000',reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='OtherInternet')
async def OtherInternet(callOtherInternet: types.CallbackQuery):
    await callOtherInternet.message.edit_text(text='Проблемы с интернетом',reply_markup=OtherInternetKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='InternetOnCashbox')
async def InternetOnCashbox(callIOC: types.CallbackQuery):
    await callIOC.message.edit_text(text='Какая ошибка',reply_markup=InternetOnCashboxKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='YellowTriangle')
async def YellowTriangle(callYT: types.CallbackQuery):
    await callYT.message.edit_text(text='[Желтый треугольник](https://downloader.disk.yandex.ru/preview/b22c342aea620ad46c15a88304f7fc573304fe4a9f812c03140655b1b39f8ba7/62ace058/JbFVi7i4XV4Zv0YKduCAPHKLjK3Tbuf5Fe8yWan6E57jkAiD7sPJ4VuuC4Vf4Gkde1m3CqwFVek9eujpawprow%3D%3D?uid=0&filename=%D0%96%D0%B5%D0%BB%D1%82%D1%8B%D0%B9%20%D1%82%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='RedCross')
async def RedCross(callRCB: types.CallbackQuery):
    await callRCB.message.edit_text(text='[Красный крестик, сетевой кабель не подключен](https://downloader.disk.yandex.ru/preview/dfbc00062b3145d2c11608c5ac2f1b108ce965b9cde813d93446b7de2e942c04/62ace1be/mgkU1n_8Vi1MNKsOdDT0yENr5e5Udatibtj0bReQGm7-X43trLRD5dGdUTvthkmKszd-NAm4833rZ-b705eMfA%3D%3D?uid=0&filename=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B9_%D0%BA%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%2C_%D1%81%D0%B5%D1%82%D0%B5%D0%B2%D0%BE%D0%B9_%D0%BA%D0%B0%D0%B1%D0%B5%D0%BB%D1%8C_%D0%BD%D0%B5_%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='InternetConnectionStatus')
async def InternetConnectionStatus(callICS: types.CallbackQuery):
    await callICS.message.edit_text(text='[Статус интернет соединения](https://downloader.disk.yandex.ru/preview/19f84a8b95831e5a9bc6033ddda9b32660bfb42911f7434d0c9b9c50a7dd6aaf/62ace2fe/jDBaigMQTnHYwbC4tRxrLENr5e5Udatibtj0bReQGm49GqOKFJtoE-pzYM66y6rsmbiQFBZcJBeKMLYkdd6KQA%3D%3D?uid=0&filename=%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%20%D1%81%D0%BE%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='NoConnectionsAvailable')
async def NoConnectionsAvailable(callNCA: types.CallbackQuery):
    await callNCA.message.edit_text(text='Если видите сообщение о том, что нет доступных подключений или сетевой кабель не подключен, значит надо проверить включен ли роутер, горит ли на нем индикация.\n'
                                          'После этого проверьте, что к компьютеру сзади подключен интернет-кабель как на картинке. Если все подключено, то необходимо обра-титься в техническую поддержку по номеру +7 965 979 0000[.](https://downloader.disk.yandex.ru/preview/56cb8b9224a7f95a97ad6adb0dcdb851225cf5427e9e5cacaa7fb96bb9d7e1f3/62ace72d/UrmWVy8I0OwS-E89lFYgvivzHcdL1yT8PRYuhcftfausgWFinoW3kJacFMAsWEFD6OAcsESJGUwPMJ9LBbLLtw%3D%3D?uid=0&filename=%D0%BD%D0%B5%D1%82%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D1%8B%D1%85%20%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B9.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)', parse_mode='Markdown',  reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='WithoutInternetAccess')
async def WithoutInternetAccess(callWIA: types.CallbackQuery):
    await callWIA.message.edit_text(text='Если вы видите желтый треугольник и сообщение «Без доступа к Ин-тернету», то необходимо презагрузить роутер.\n'
                                          ' Отключить его из розетки, по-дождать минуту и подключить обратно. Подождите 5 минут, если не зарабо-тал, то необходимо обратиться к провайдеру, который предоставляет интернет. ',reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')


#Блок проблем с безналом
@dp.callback_query_handler(text='CashlessPayment')
async def CashlessPayment(callCP: types.CallbackQuery):
    await callCP.message.edit_text(text='Выберите раздел проблемы',reply_markup=CashlessPaymentKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='ProblemWithPaymentOrders')
async def ProblemWithPaymentOrders(callPWPO: types.CallbackQuery):
    await callPWPO.message.edit_text(text='Проблема с оплатой заказов',reply_markup=ProblemWithPaymentOrdersKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='ProblemsAfterOrderPayment')
async def ProblemsAfterOrderPayment(callPAOP: types.CallbackQuery):
    await callPAOP.message.edit_text(text='Проблемы возникшие после оплаты заказа',reply_markup=ProblemsAfterOrderPaymentKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='ProblemsPaymentForTheOrder')
async def ProblemsPaymentForTheOrder(callPPFTO: types.CallbackQuery):
    await callPPFTO.message.edit_text(text='Проблемы связанные с безналичной оплатой заказа', reply_markup=ProblemsPaymentForTheOrderKeyboard)
    logger.debug('Пользователь нажал кнопку "Проблемы связанные с безналичной оплатой заказа"')

#Проблема с оплатой заказов

@dp.callback_query_handler(text='NoCommunicationWithDevice')
async def ProblemsPaymentForTheOrder(callPPFTO: types.CallbackQuery):
    await callPPFTO.message.edit_text(text='Проверить, включен ли фискальный регистратор, так-же проверить качество подключения проводов к нему (питание+USB провода).\n'
                                        'Так-же проверить подключение USB провода со стороны компьютера.\n'
                                        'Если вышеперечисленные действия не помогли, то свяжитесь с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='FailedToGetDeviceSerialNumber')
async def FailedToGetDeviceSerialNumber(callFTGDN: types.CallbackQuery):
    await callFTGDN.message.edit_text(text='Выключить фискальный регистратор на кнопку и включить заново.\n'
                                        'Завершить процесс IIKO через диспетчер задач, запустить IIKO заново и повторить оплату.\n'
                                        'Если вышеперечисленные действия не помогли, то свяжитесь с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='FNStorageResourceExhausted')
async def FNStorageResourceExhausted(callFNSRE: types.CallbackQuery):
    await callFNSRE.message.edit_text(text='Связаться с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='FailedToSetOperatingMode')
async def FailedToSetOperatingMode(callFTSOM: types.CallbackQuery):
    await callFTSOM.message.edit_text(text='Вчера сотрудники забыли закрыть кассовую смену.\n'
                                        'Закрываем кассовую смену через iiko.\n'
                                        'Текущий заказ можно удалить и пробить в актуальной смене.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='FailedToCloseCheck')
async def FailedToCloseCheck(callFTCC: types.CallbackQuery):
    await callFTCC.message.edit_text(text='Связаться с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='FailedToGetPaymentMethod')
async def FailedToGetPaymentMethod(callFTGPM: types.CallbackQuery):
    await callFTGPM.message.edit_text(text='Связаться с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='NotSupportedInThisDeviceMode')
async def NotSupportedInThisDeviceMode(callNSITDM: types.CallbackQuery):
    await callNSITDM.message.edit_text(text='Необходимо выключить и включить фискальный регистратор и перезагрузить программу IIKO.\n'
                                         'Если вышеперечисленные действия не помогли, то свяжитесь с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='WPayingForTheOrderPrepaymentWindowAppears')
async def WPayingForTheOrderPrepaymentWindowAppears(callWPFTOPWA: types.CallbackQuery):
    await callWPFTOPWA.message.edit_text(text='1.Нажимаем кнопку "Отмена"\n'
                                           '2. Удаляем тип оплаты "Предоплата", нажимая на крестик\n'
                                           '3. Выбираем нужный тип оплаты, вводим сумму и снова оплачиваем заказ', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

#Проблемы возникшие после оплаты заказа

@dp.callback_query_handler(text='NoConnectionToOFDNumberOfUnsentDocuments')
async def NoConnectionToOFDNumberOfUnsentDocuments(callNCTOFDNOUD: types.CallbackQuery):
    await callNCTOFDNOUD.message.edit_text(text='Такое уведомление ВСЕГДА появляется после каждого закрытого заказа. \n'
                                           'Если в данном уведомлении количество документов больше, чем ,,1,,,  необходимо обратиться в техническую поддержку.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='AnErrorOccurredWhilePrintingTheReceipt')
async def AnErrorOccurredWhilePrintingTheReceipt(callAEOWPTR: types.CallbackQuery):
    await callAEOWPTR.message.edit_text(text='Ошибка говорит о том, что фискальный регистратор не видет чековую ленту, либо она отстутсвует\n'
                                           'Если ошибка возникла при замене рулона на новый, откройте крышку фискальника и отмотайте с рулона небольшое количество ленты.\n'
                                           'Далее закройте крышку и повторите оплату заказа.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')


#Проблемы связанные с безналичной оплатой заказа
@dp.callback_query_handler(text='PaymentTypeBankCardDoesNotWork')
async def PaymentTypeBankCardDoesNotWork(callPTBCDNW: types.CallbackQuery):
    await callPTBCDNW.message.edit_text(text='Перезагрузите компьютер.\n'
                                           'Если не помогло, то свяжитесь с оператором', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='BankTerminalNotWorkingBlackScreen')
async def BankTerminalNotWorkingBlackScreen(callBTNWBS: types.CallbackQuery):
    await callBTNWBS.message.edit_text(text='Перезагрузите компьютер.\n'
                                           'Если после перезагрузки терминал не заработал, перевоткните провода, которые идут от банковского терминала и повторно перезагрузите компьютер.\n'
                                           'Если ничего не помогло, то звоните в банк, который вас обслуживает.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='ThereIsNoBankCardPayment')
async def ThereIsNoBankCardPayment(callTINBCP: types.CallbackQuery):
    await callTINBCP.message.edit_text(text='Пишите в техподдержу с приложением фото отсутсвия данного типа оплаты.', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

#Блок "По доставке"
@dp.callback_query_handler(text='Delivery')
async def Delivery(callDelivery: types.CallbackQuery):
    await callDelivery.message.edit_text(text='Выберете раздел проблемы', reply_markup=DeliveryKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')


@dp.callback_query_handler(text='NoPermissionToSell')
async def NoPermissionToSell(callNPTS: types.CallbackQuery):
    await callNPTS.message.edit_text(text='Необходимо обратиться к специалисту по ценообразованию Евтиной Дарье +7-913-680-80-90',
                                     reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='DisabledOnPoint')
async def DisabledOnPoint(callDOP: types.CallbackQuery):
    await callDOP.message.edit_text(text='Связаться с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='CannotBeTransferred')
async def CannotBeTransferred(callCBT: types.CallbackQuery):
    await callCBT.message.edit_text(text='Необходимо обратиться в службу доставки по тел. 8-800-700-67-76',
                                    reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='PointOfSaleNotSynced')
async def PointOfSaleNotSynced(callPOSNS: types.CallbackQuery):
    await callPOSNS.message.edit_text(text='Необходимо обратиться в службу доставки по тел. 8-800-700-67-76',
                                      reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='RequestErrorInIIKO')
async def RequestErrorInIIKO(callREII: types.CallbackQuery):
    await callREII.message.edit_text(text='Связаться с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='TheRequiredPaymentType')
async def TheRequiredPaymentType(callTRPT: types.CallbackQuery):
    await callTRPT.message.edit_text(text='Связаться с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

#Блок проблемы в офисе

# @dp.callback_query_handler(text='ProblemsInTheOffice')
# async def ProblemsInTheOffice(callPITO: types.CallbackQuery):
#     await callPITO.message.edit_text(text='Какая у вас проблема', reply_markup=ProblemsInTheOfficeKeyboard)
#     logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='RemoteNotWorking')
async def RemoteNotWorking(callRNW: types.CallbackQuery):
    await callRNW.message.edit_text(text='Нажмите сочетание клавиш ctrl+alt+end. Далее нажмите "выйти"\n'
                                       'Если не помогло (кнопка, по которой переход на структуру ниже)\n'
                                       '1) Требуется открыть Сайт https://rds.itfood.ru\n'
                                       '2) Ввести свой логин (Фамилия@rds.itfood.ru) и пароль \n'
                                       'Если пускает на сайт, скачать ярлык удаленки и авторизоваться через него \n'
                                       'Если не пускает через новый ярлык обратиться в техническую поддержку\n'
                                       'Если не пускает на сайт обратиться в техническую поддержку', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Какие продукты рекомендовать"')

@dp.callback_query_handler(text='MailProblem')
async def MailProblem(callMP: types.CallbackQuery):
    await callMP.message.edit_text(text='Необходимо связаться с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

# @dp.callback_query_handler(text='NoAccessToRMS')
# async def NoAccessToRMS(callNATRMS: types.CallbackQuery):
#     await callNATRMS.message.edit_text(text='Какая проблема', reply_markup=NoAccessToRMSKeyboard)
#     logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='LicenseRestriction')
async def LicenseRestriction(callLR: types.CallbackQuery):
    await callLR.message.edit_text(text='Необходимо связаться с техподдержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='NoAccessToTheServer')
async def NoAccessToTheServer(callNATHS: types.CallbackQuery):
    await callNATHS.message.edit_text(text='Проверьте, что все данные введены верно и выбран нужный РМС. ', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

# @dp.callback_query_handler(text='ChainProblem')
# async def ChainProblem(callCP: types.CallbackQuery):
#     await callCP.message.edit_text(text='Проблема работы с чейном[.](https://downloader.disk.yandex.ru/preview/e09460847d377af5608a91f0afe6b05f80350d7652402db5aac561c5e840a8dd/62ada0ab/GZ6ue5U6azFiZG2A22dLBK5bqM_xoyxzFLuVJEgQ4VmApg5Hbhyvz0UmC9rbUtcsW9cKY9sxub0Ybi3QkTQRXQ%3D%3D?uid=0&filename=%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D1%8B%20%D1%81%20%D1%87%D0%B5%D0%B9%D0%BD%D0%BE%D0%BC.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=ChainProblemKeyboard)
#     logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='NoAccessToTheServerChain')
async def NoAccessToTheServerChain(callNATTSC: types.CallbackQuery):
    await callNATTSC.message.edit_text(text='Проверьте, что все данные введены верно и выбран нужный чейн. ', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='ServerIsNotAnIIKO_RMS')
async def ServerIsNotAnIIKO_RMS(callSINAIIKO: types.CallbackQuery):
    await callSINAIIKO.message.edit_text(text='Вы зашли не в ту программу, откройте Iiko Chain Operations', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

# @dp.callback_query_handler(text='ThePrinterIsNotWorking')
# async def ThePrinterIsNotWorking(callTPINW: types.CallbackQuery):
#     await callTPINW.message.edit_text(text='Какая ошибка:', reply_markup=ThePrinterIsNotWorkingKeyboard)
#     logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='TheRedLightIsOn')
async def TheRedLightIsOn(callTRLIO: types.CallbackQuery):
    await callTRLIO.message.edit_text(text='Горит красная лампочка[.](https://downloader.disk.yandex.ru/preview/6ee9f33c09b2b7c725515ee8a634119653526779f78499bd2544ee4402607f83/62ada3bd/x2x0eXjAEGU5P7NTgB8JCHKLjK3Tbuf5Fe8yWan6E571q0ksErggXOItoggv-AdgDN4y4TzPIcL8FxPe-ysDHw%3D%3D?uid=0&filename=%D0%93%D0%BE%D1%80%D0%B8%D1%82%20%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%B0%D1%8F%20%D0%BB%D0%B0%D0%BC%D0%BF%D0%BE%D1%87%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='CartridgeReplacement')
async def CartridgeReplacement(callCR: types.CallbackQuery):
    await callCR.message.edit_text(text='Замена картриджа[.](https://downloader.disk.yandex.ru/preview/1ec07ce4453834768deac1a6ae919c2f7e6ea222d891fde3052dba40e85ba939/62ada4a0/rUMg5EvJQG9BkU51jTsu7Qg1Z-aWW0T3iycPDE0GAbD3g6-DwDpgyOtFX2DNOI_RbxpnhvFuVdzJBFGVR7NIGQ%3D%3D?uid=0&filename=%D0%97%D0%B0%D0%BC%D0%B5%D0%BD%D0%B0%20%D0%BA%D0%B0%D1%80%D1%82%D1%80%D0%B8%D0%B4%D0%B6%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='PaperJam')
async def PaperJam(callPJ: types.CallbackQuery):
    await callPJ.message.edit_text(text='Замятие бумаги[.](https://downloader.disk.yandex.ru/preview/8c34b0686a22c409d1af56f87d857b488fdb6a3ba06fdaf403747359f9bcc1eb/62ada51d/F7CcQnnbpI0znnFPCRe2oENr5e5Udatibtj0bReQGm7hC6cogl5SUTO09Fqzv1hgtjkvOVSsyfpbfWlgf6lfaw%3D%3D?uid=0&filename=%D0%97%D0%B0%D0%BC%D1%8F%D1%82%D0%B8%D0%B5%20%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B8.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='DoesntPickUpPaper')
async def DoesntPickUpPaper(callDPUP: types.CallbackQuery):
    await callDPUP.message.edit_text(text='Не захватывает бумагу[.](https://downloader.disk.yandex.ru/preview/2200bdca4aff74a993f319909df609cc88e50cc645b8fcbd8f9e1c15fd90400d/62ada5b6/GebBYtHOvmeosMGf8FO0KENr5e5Udatibtj0bReQGm7HeBd2IcR7xPOWIBmfeP3IQ4KRPfGogVH5MbFleOAdOA%3D%3D?uid=0&filename=%D0%9D%D0%B5%20%D0%B7%D0%B0%D1%85%D0%B2%D0%B0%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%20%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D1%83.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='TheScannerDoesNotWork')
async def TheScannerDoesNotWork(callTSDNW: types.CallbackQuery):
    await callTSDNW.message.edit_text(text='Ошибка "Освободите блокиратор[.](https://downloader.disk.yandex.ru/preview/7988bcc0653b181632b3fb9cf1e9a2ad976ed68ecc595f29137ddeb148212320/62adac2b/Ix2bbpCmQXgOkbvzRq1iOENr5e5Udatibtj0bReQGm5G3PEtPaqaOP2SNF_0YYSZEWMm0JVOlTwoL75h8hqfxw%3D%3D?uid=0&filename=%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0%20%D0%9E%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%20%D0%B1%D0%BB%D0%BE%D0%BA%D0%B8%D1%80%D0%B0%D1%82%D0%BE%D1%80.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)"',parse_mode='Markdown', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "Еще"')

@dp.callback_query_handler(text='Other')
async def Other(callOther: types.CallbackQuery):
    await callOther.message.edit_text(text='Связаться с тех поддержкой', reply_markup=callTechSuppKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

#Кнопка возврата
@dp.callback_query_handler(text='backToMainMenu')
async def backToMainMenu(callbTMM: types.CallbackQuery):
    await callbTMM.message.edit_text(text='Выберите интересующий раздел', reply_markup=firstMenuKeyboard)

@dp.callback_query_handler(text='backToMainMenuKeyboard')
async def backToMainMenuKeyboard(callbTMMk: types.CallbackQuery):
    await callbTMMk.message.edit_text(text='Выберите интересующий раздел', reply_markup=firstMenuKeyboard)

@dp.callback_query_handler(text='backToIIKOKeyboard')
async def backToIIKOKeyboard(callbtIIKO: types.CallbackQuery):
    await callbtIIKO.message.edit_text(text='Выберите раздел проблемы', reply_markup=IIKOKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToErrorsToOrderStatusesAndProgramOperationKeyboard')
async def backToErrorsToOrderStatusesAndProgramOperationKeyboard(callbtETOSAPOK: types.CallbackQuery):
    await callbtETOSAPOK.message.edit_text(text='Ошибки связанные со статусами заказов и работы программы:', reply_markup=ErrorsToOrderStatusesAndProgramOperationKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToErrorsTheOpeningAndClosingOfTheCashRegisterShiftKeyboard')
async def backToErrorsTheOpeningAndClosingOfTheCashRegisterShiftKeyboard(callbtETOACOTCRSK: types.CallbackQuery):
    await callbtETOACOTCRSK.message.edit_text(text='Ошибки связанные с открытием и закрытием кассовой смены:', reply_markup=ErrorsTheOpeningAndClosingOfTheCashRegisterShiftKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToFRButtonKeyboard')
async def backToFRButtonKeyboard(callbtFRBK: types.CallbackQuery):
    await callbtFRBK.message.edit_text(text='Выберите интересующий раздел', reply_markup=FRButtonKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToProblemsPayKeyboard')
async def backToProblemsPayKeyboard(callbtPPK: types.CallbackQuery):
    await callbtPPK.message.edit_text(text='Проблемы при попытке оплатить заказ', reply_markup=FRButtonKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToCashBoxProblemsKeyboard')
async def backToCashBoxProblemsKeyboard(callbtCBPK: types.CallbackQuery):
    await callbtCBPK.message.edit_text(text='Проблемы с кассой', reply_markup=FRButtonKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToOtherFRKeyboard')
async def backToOtherFRKeyboard(callbtOFRK: types.CallbackQuery):
    await callbtOFRK.message.edit_text(text='Какая проблема:', reply_markup=FRButtonKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToscreenKeyboard')
async def backToscreenKeyboard(callbTSKK: types.CallbackQuery):
    await callbTSKK.message.edit_text(text='Выберите интересующий раздел', reply_markup=firstMenuKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToCashlessPaymentKeyboard')
async def backToCashlessPaymentKeyboard(callbtCPK: types.CallbackQuery):
    await callbtCPK.message.edit_text(text='Выберите раздел проблемы', reply_markup=CashlessPaymentKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')



@dp.callback_query_handler(text='backToProblemsAfterOrderPaymentKeyboard')
async def backToProblemsAfterOrderPaymentKeyboard(callbtPAOPK: types.CallbackQuery):
    await callbtPAOPK.message.edit_text(text='Проблемы возникшие после оплаты заказа', reply_markup=ProblemsAfterOrderPaymentKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToProblemWithPaymentOrdersKeyboard')
async def backToProblemWithPaymentOrdersKeyboard(callbtPWPOK: types.CallbackQuery):
    await callbtPWPOK.message.edit_text(text='Проблема с оплатой заказов', reply_markup=ProblemWithPaymentOrdersKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToProblemsPaymentForTheOrderKeyboard')
async def backToProblemsPaymentForTheOrderKeyboard(callbtPPFTOK: types.CallbackQuery):
    await callbtPPFTOK.message.edit_text(text='Проблемы связанные с безналичной оплатой заказа', reply_markup=ProblemsPaymentForTheOrderKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToInternetKeyboard')
async def backToInternetKeyboard(callbtIK: types.CallbackQuery):
    await callbtIK.message.edit_text(text='Проблемы с интернетом', reply_markup=InternetKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToInternetOnCashboxKeyboard')
async def backToInternetOnCashboxKeyboard(callbtIOCK: types.CallbackQuery):
    await callbtIOCK.message.edit_text(text='Какая ошибка', reply_markup=InternetOnCashboxKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToOtherInternetKeyboard')
async def backToOtherInternetKeyboard(callbtOIK: types.CallbackQuery):
    await callbtOIK.message.edit_text(text='Проблемы с интернетом', reply_markup=OtherInternetKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToDeliveryKeyboard')
async def backToDeliveryKeyboard(callbtTDK: types.CallbackQuery):
    await callbtTDK.message.edit_text(text='Выберете раздел проблемы', reply_markup=DeliveryKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')

@dp.callback_query_handler(text='backToElectronicQueueAndTVKeyboard')
async def backToElectronicQueueAndTVKeyboard(callbtEQATVK: types.CallbackQuery):
    await callbtEQATVK.message.edit_text(text='Какая ошибка:', reply_markup=ElectronicQueueAndTVKeyboard)
    logger.debug('Пользователь нажал кнопку "QR-код"')


@dp.callback_query_handler(text='callTechSupp')
async def callTechSupp(calltsupp:types.Message):
    await ForwMess.Forward_message.set()
    await bot.send_message(calltsupp.from_user.id, 'Пожалуйста, опишите свою проблему детальнее одним сообщением')
# -1001673754768 channel
# -1001645401143 group


@dp.message_handler(state=ForwMess.Forward_message)
async def forward_message(message: types.Message, state: FSMContext):
    await bot.send_message('-1001673754768', f'НОВАЯ ЗАЯВКА! \n'
                                             f'От: @{message.from_user.username} \n'
                                             f'Описание проблемы: {message.text}')
    await bot.send_message(message.from_user.id, text='Ваша заявка отправлена. \n'
                                                      'Обратите внимание, техподдержка работает с 8:00 до 00:00')

    # await bot.forward_message(chat_id='-1001645401143',
    #                           from_chat_id=message.from_user.id,
    #                           message_id=message.message_id)
    await state.finish()


# @dp.message_handler(commands='get_id')
# async def callTechSupp(callTSupppp : types.Message):
#     chatid = callTSupppp.chat.id
#     await bot.send_message(callTSupppp.from_user.id, text=chatid)



#https://t.me/+wGeFnHb6ACBkOWFi

# @dp.callback_query_handler(text='helpButton')
# async def helpMessage(helpMessage : types.Message):
#     await helpMessage.answer('Оператор скоро вам ответит')

@dp.message_handler(content_types=['text'])
async def messageKeyboard(message):
    if message.text == "Проверка":
        await bot.send_message(message.from_user.id, 'Проверка была',reply_markup=firstMenuKeyboard)
    else:
        await bot.send_message(message.from_user.id,'Бот работает только с кнопками. Выберите интересующий раздел',reply_markup=firstMenuKeyboard)

executor.start_polling(dp,skip_updates=True)




