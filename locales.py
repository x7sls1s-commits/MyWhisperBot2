from locales_dict import Locale, LocalesDict

locale_ar = Locale()

locales = LocalesDict({
    'ar': locale_ar
}, locale_ar)


# TOO_LONG_TITLE
locale_ar.too_long_title = '⚠️ رسالتك طويلة جدًا!'


# FOR_TITLE
locale_ar.for_title = '🔒 إلى %s'


# EXCEPT_TITLE
locale_ar.except_title = '🔒 للجميع باستثناء %s'


# SPOILER_TITLE
locale_ar.spoiler_title = '🔒 همسة'


# TOO_LONG_MESSAGE
locale_ar.too_long_message = (
    '🥺 عذرًا، لا يمكن إرسال رسالتك لأنها تتجاوز الحد المسموح به وهو 500 حرف.'
)


# FOR_MESSAGE
locale_ar.for_message = (
    '🔒 رسالة سرية إلى %s، لا يمكن فتحها إلا من قِبله.'
)


# EXCEPT_MESSAGE
locale_ar.except_message = (
    '🔒 رسالة سرية للجميع باستثناء %s، يمكن للآخرين فقط فتحها.'
)


# SPOILER_MESSAGE
locale_ar.spoiler_message = (
    '🔒 همسة سرية! يمكن للجميع عرضها '
)


# GROUP_GREETING_MESSAGE
locale_ar.group_greeting_message = (
    "👋 *مرحبًا! أنا %s*\n\n"
    "🔒 أساعدك على إرسال رسائل سرية لا يمكن رؤيتها إلا من الأشخاص المحددين.\n\n"
    "💡 للبدء: /start@%s"
)


# INFO_MESSAGE
locale_ar.info_message = (
    "🔐 يمكنك إرسال رسائل سرية ومشاركتها مع الأشخاص بطريقة بسيطة وآمنة."
)


# HOW_TO_USE
locale_ar.how_to_use = '💡 كيفية استخدام هذا البوت؟'


# TOO_LONG_DESCRIPTION
locale_ar.too_long_description = (
    '✂️ عذرًا! الرسالة طويلة جدًا! (الحد الأقصى 500 حرف)'
)


# NOT_ALLOWED
locale_ar.not_allowed = (
    '🔐 عذرًا، لا يمكنك فتح هذه الهمسة.'
)


# NOT_ACCESSIBLE
locale_ar.not_accessible = (
    '⌛ هذا المحتوى لم يعد متاحًا.'
)


# VIEW
locale_ar.view = 'عرض الرسالة 🔒'


# AND_CONNECTOR
locale_ar.and_connector = 'و'
