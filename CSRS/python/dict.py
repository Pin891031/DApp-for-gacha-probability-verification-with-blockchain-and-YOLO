def convertNametoCardNumber(name):
    name_to_cardNumber = {
        '日和': 'C3', '怜': 'C4', '禊': 'C5', '胡桃': 'C6', '依里': 'C7', '鈴莓': 'C8', '優花梨': 'C9', '碧': 'C10', '美咲': 'C11', '步未': 'C12',
        '莉瑪': 'C13', '茉莉': 'C14', '茜里': 'C15', '宮子': 'C16', '雪': 'C17', '七七香': 'C18', '美里': 'C19', '鈴奈': 'C20', '香織': 'C21', '美美': 'C22',
        '綾音': 'C23', '鈴': 'C24', '惠理子': 'C25', '忍': 'C26', '真陽': 'C27', '栞': 'C28', '千歌': 'C29', '空花': 'C30', '珠希': 'C31', '美冬': 'C32',
        '深月': 'C33', '紡希': 'C34', '純(聖誕節)': 'C35', '杏奈': 'C36', '真步': 'C37', '璃乃': 'C38', '初音': 'C39', '霞': 'C40', '伊緒': 'C41', '咲戀': 'C42',
        '望': 'C43', '妮諾': 'C44', '秋乃': 'C45', '鏡華': 'C46', '智': 'C47', '真琴': 'C48', '伊莉亞': 'C49', '純': 'C50', '靜流': 'C51', '莫妮卡': 'C52',
        '流夏': 'C53', '吉塔': 'C54', '亞里莎': 'C55', '雪菲': 'C56', '嘉夜': 'C57', '祈梨': 'C58', '安': 'C59', '古蕾婭': 'C60', '空花(大江戶)': 'C61', '妮諾(大江戶)': 'C62',
        '碧(插班生)': 'C63', '克蘿依': 'C64', '琪愛兒': 'C65', '優妮': 'C66', '美美(萬聖節)': 'C67', '露娜': 'C68', '伊莉亞(聖誕節)': 'C69', '霞(魔法少女)': 'C70', '鈴(遊俠)': 'C71', '真陽(遊俠)': 'C72',
        '璃乃(奇幻)': 'C73', '七七香(夏日)': 'C74', '純(夏日)': 'C75', '茜里(天使)': 'C76', '依里(天使)': 'C77', '伶(萬聖節)': 'C78', '莫妮卡(魔法少女)': 'C79', '智(魔法少女)': 'C80', '咲戀(聖誕節)': 'C81', '霞(夏日)': 'C82',
        '真琴(灰姑娘)': 'C83', '真步(灰姑娘)': 'C84', '克蘿依(聖學祭)': 'C85', '琪愛兒(聖學祭)': 'C86', '優妮(聖學祭)': 'C87', '祈梨(時空旅者)': 'C88', '嘉夜(時空旅者)': 'C89', '碧(工作服)': 'C90', '美冬(工作服)': 'C91', '靜流(夏日)': 'C92',
        '千歌(夏日)': 'C93', '深月(大江戶)': 'C94', '雪(大江戶)': 'C95', '鈴奈(萬聖節)': 'C96', '伊緒(黑暗)': 'C97', '空花(黑暗)': 'C98', '璃乃(聖誕節)': 'C99', '胡桃(舞台)': 'C100', '美咲(舞台)': 'C101', '祈梨(怪盜)': 'C102',
        '杏奈(海盜)': 'C103', '忍(海盜)': 'C104', '優花梨(露營)': 'C105', '班比': 'C106', '優依(夏日)': 'C107', '鏡華(夏日)': 'C108', '真步(探險家)': 'C109', '綾音(探險家)': 'C110', '七七香(萬聖節)': 'C111', '茉莉(狂野)': 'C112',
        '矛依未': 'C113', '帆稀': 'C114', '拉比林斯達': 'C115', '似似花': 'C116', '克莉絲提娜': 'C117', '蘭法': 'C118', '美空': 'C119', '愛梅斯': 'C120', '日和(公主)': 'C121', '優依(公主)': 'C122',
        '伶(公主)': 'C123', '貪吃佩可(公主)': 'C124', '可可蘿(公主)': 'C125', '凱留(公主)': 'C126', '初音＆栞': 'C127', '禊＆美美＆鏡華': 'C128', '秋乃＆咲戀': 'C129', '安＆古蕾婭': 'C130', '貪吃佩可(夏日)': 'C131', '鈴莓(夏日)': 'C132',
        '凱留(夏日)': 'C133', '珠希(夏日)': 'C134', '忍(萬聖節)': 'C135', '美咲(萬聖節)': 'C136', '千歌(聖誕節)': 'C137', '綾音(聖誕節)': 'C138', '日和(新年)': 'C139', '優衣(新年)': 'C140', '靜流(情人節)': 'C141', '鈴奈(夏日)': 'C142',
        '咲戀(夏日)': 'C143', '真琴(夏日)': 'C144', '真步(夏日)': 'C145', '鏡華(萬聖節)': 'C146', '克莉絲提娜(聖誕節)': 'C147', '貪吃佩可(新年)': 'C148', '可可蘿(新年)': 'C149', '凱留(新年)': 'C150', '流夏(夏日)': 'C151', '初音(夏日)': 'C152',
        '紡希(萬聖節)': 'C153', '秋乃(聖誕節)': 'C154', '似似花(新年)': 'C155', '可可蘿(祭服)': 'C156', '惠理子(夏日)': 'C157', '望(夏日)': 'C158', '香織(萬聖節)': 'C159', '宮子(聖誕節)': 'C160', '雪菲(新年)': 'C161', '伊莉亞(新年)': 'C162',
        '克蕾琪塔': 'C163', '貪吃佩可(超載)': 'C164', '凱留(超載)': 'C165', '步未(怪盜)': 'C166', '靜流(黑暗)': 'C167', '伶(夏日)': 'C168', '美美(夏日)': 'C169', '涅婭': 'C170', '智(萬聖節)': 'C171', '克莉絲提娜(狂野)': 'C172',
        '茜里(聖誕節)': 'C173', '帆稀(新年)': 'C174', '美里(新年)': 'C175', '望(解放者)': 'C176', '矛依未(解放者)': 'C177',
        
    }

    if name in name_to_cardNumber:
        return name_to_cardNumber[name]
    else:
        return None  # 找不到就返回none
    
def convertCardNumbertoName(name):
    cardNumber_to_name = {
        'C3': '日和', 'C4': '怜', 'C5': '禊', 'C6': '胡桃', 'C7': '依里', 'C8': '鈴莓', 'C9': '優花梨', 'C10': '碧', 'C11': '美咲', 'C12': '步未',
        'C13': '莉瑪', 'C14': '茉莉', 'C15': '茜里', 'C16': '宮子', 'C17': '雪', 'C18': '七七香', 'C19': '美里', 'C20': '鈴奈', 'C21': '香織', 'C22': '美美',
        'C23': '綾音', 'C24': '鈴', 'C25': '惠理子', 'C26': '忍', 'C27': '真陽', 'C28': '栞', 'C29': '千歌', 'C30': '空花', 'C31': '珠希', 'C32': '美冬',
        'C33': '深月', 'C34': '紡希', 'C35': '純(聖誕節)', 'C36': '杏奈', 'C37': '真步', 'C38': '璃乃', 'C39': '初音', 'C40': '霞', 'C41': '伊緒', 'C42': '咲戀',
        'C43': '望', 'C44': '妮諾', 'C45': '秋乃', 'C46': '鏡華', 'C47': '智', 'C48': '真琴', 'C49': '伊莉亞', 'C50': '純', 'C51': '靜流', 'C52': '莫妮卡',
        'C53': '流夏', 'C54': '吉塔', 'C55': '亞里莎', 'C56': '雪菲', 'C57': '嘉夜', 'C58': '祈梨', 'C59': '安', 'C60': '古蕾婭', 'C61': '空花(大江戶)', 'C62': '妮諾(大江戶)',
        'C63': '碧(插班生)', 'C64': '克蘿依', 'C65': '琪愛兒', 'C66': '優妮', 'C67': '美美(萬聖節)', 'C68': '露娜', 'C69': '伊莉亞(聖誕節)', 'C70': '霞(魔法少女)', 'C71': '鈴(遊俠)', 'C72': '真陽(遊俠)',
        'C73': '璃乃(奇幻)', 'C74': '七七香(夏日)', 'C75': '純(夏日)', 'C76': '茜里(天使)', 'C77': '依里(天使)', 'C78': '伶(萬聖節)', 'C79': '莫妮卡(魔法少女)', 'C80': '智(魔法少女)', 'C81': '咲戀(聖誕節)', 'C82': '霞(夏日)',
        'C83': '真琴(灰姑娘)', 'C84': '真步(灰姑娘)', 'C85': '克蘿依(聖學祭)', 'C86': '琪愛兒(聖學祭)', 'C87': '優妮(聖學祭)', 'C88': '祈梨(時空旅者)', 'C89': '嘉夜(時空旅者)', 'C90': '碧(工作服)', 'C91': '美冬(工作服)', 'C92': '靜流(夏日)',
        'C93': '千歌(夏日)', 'C94': '深月(大江戶)', 'C95': '雪(大江戶)', 'C96': '鈴奈(萬聖節)', 'C97': '伊緒(黑暗)', 'C98': '空花(黑暗)', 'C99': '璃乃(聖誕節)', 'C100': '胡桃(舞台)', 'C101': '美咲(舞台)', 'C102': '祈梨(怪盜)',
        'C103': '杏奈(海盜)', 'C104': '忍(海盜)', 'C105': '優花梨(露營)', 'C106': '班比', 'C107': '優依(夏日)', 'C108': '鏡華(夏日)', 'C109': '真步(探險家)', 'C110': '綾音(探險家)', 'C111': '七七香(萬聖節)', 'C112': '茉莉(狂野)',
        'C113': '矛依未', 'C114': '帆稀', 'C115': '拉比林斯達', 'C116': '似似花', 'C117': '克莉絲提娜', 'C118': '蘭法', 'C119': '美空', 'C120': '愛梅斯', 'C121': '日和(公主)', 'C122': '優依(公主)',
        'C123': '伶(公主)', 'C124': '貪吃佩可(公主)', 'C125': '可可蘿(公主)', 'C126': '凱留(公主)', 'C127': '初音＆栞', 'C128': '禊＆美美＆鏡華', 'C129': '秋乃＆咲戀', 'C130': '安＆古蕾婭', 'C131': '貪吃佩可(夏日)', 'C132': '鈴莓(夏日)',
        'C133': '凱留(夏日)', 'C134': '珠希(夏日)', 'C135': '忍(萬聖節)', 'C136': '美咲(萬聖節)', 'C137': '千歌(聖誕節)', 'C138': '綾音(聖誕節)', 'C139': '日和(新年)', 'C140': '優衣(新年)', 'C141': '靜流(情人節)', 'C142': '鈴奈(夏日)',
        'C143': '咲戀(夏日)', 'C144': '真琴(夏日)', 'C145': '真步(夏日)', 'C146': '鏡華(萬聖節)', 'C147': '克莉絲提娜(聖誕節)', 'C148': '貪吃佩可(新年)', 'C149': '可可蘿(新年)', 'C150': '凱留(新年)', 'C151': '流夏(夏日)', 'C152': '初音(夏日)',
        'C153': '紡希(萬聖節)', 'C154': '秋乃(聖誕節)', 'C155': '似似花(新年)', 'C156': '可可蘿(祭服)', 'C157': '惠理子(夏日)', 'C158': '望(夏日)', 'C159': '香織(萬聖節)', 'C160': '宮子(聖誕節)', 'C161': '雪菲(新年)', 'C162': '伊莉亞(新年)',
        'C163': '克蕾琪塔', 'C164': '貪吃佩可(超載)', 'C165': '凱留(超載)', 'C166': '步未(怪盜)', 'C167': '靜流(黑暗)', 'C168': '伶(夏日)', 'C169': '美美(夏日)', 'C170': '涅婭', 'C171': '智(萬聖節)', 'C172': '克莉絲提娜(狂野)',
        'C173': '茜里(聖誕節)', 'C174': '帆稀(新年)', 'C175': '美里(新年)', 'C176': '望(解放者)', 'C177': '矛依未(解放者)',
    }
    if name in cardNumber_to_name:
        return cardNumber_to_name[name]
    else:
        return None  # 找不到就返回none


def characterCount(getUplaoddata):
    #getUplaoddata = [0, 0, 0, 0, 8, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    
    character_names = [
        '日和', '怜', '禊', '胡桃', '依里', '鈴莓', '優花梨', '碧', '美咲', '步未', 
        '莉瑪', '茉莉', '茜里', '宮子', '雪', '七七香', '美里', '鈴奈', '香織', '美美',
        '綾音', '鈴', '惠理子', '忍', '真陽', '栞', '千歌', '空花', '珠希', '美冬', 
        '深月', '紡希', '純(聖誕節)', '杏奈', '真步', '璃乃', '初音', '霞', '伊緒', '咲戀',
        '望', '妮諾', '秋乃', '鏡華', '智', '真琴', '伊莉亞', '純', '靜流', '莫妮卡', 
        '流夏', '吉塔', '亞里莎', '雪菲', '嘉夜', '祈梨', '安', '古蕾婭', '空花(大江戶)', '妮諾(大江戶)',
        '碧(插班生)', '克蘿依', '琪愛兒', '優妮', '美美(萬聖節)', '露娜', '伊莉亞(聖誕節)', '霞(魔法少女)', '鈴(遊俠)', '真陽(遊俠)', 
        '璃乃(奇幻)', '七七香(夏日)', '純(夏日)', '茜里(天使)', '依里(天使)', '伶(萬聖節)', '莫妮卡(魔法少女)', '智(魔法少女)', '咲戀(聖誕節)', '霞(夏日)',
        '真琴(灰姑娘)', '真步(灰姑娘)', '克蘿依(聖學祭)', '琪愛兒(聖學祭)', '優妮(聖學祭)', '祈梨(時空旅者)', '嘉夜(時空旅者)', '碧(工作服)', '美冬(工作服)', '靜流(夏日)', 
        '千歌(夏日)', '深月(大江戶)', '雪(大江戶)', '鈴奈(萬聖節)', '伊緒(黑暗)', '空花(黑暗)', '璃乃(聖誕節)', '胡桃(舞台)', '美咲(舞台)', '祈梨(怪盜)',
        '杏奈(海盜)', '忍(海盜)', '優花梨(露營)', '班比', '優依(夏日)', '鏡華(夏日)', '真步(探險家)', '綾音(探險家)', '七七香(萬聖節)', '茉莉(狂野)', 
        '矛依未', '帆稀', '拉比林斯達', '似似花', '克莉絲提娜', '蘭法', '美空', '愛梅斯', '日和(公主)', '優依(公主)',
        '伶(公主)', '貪吃佩可(公主)', '可可蘿(公主)', '凱留(公主)', '初音＆栞', '禊＆美美＆鏡華', '秋乃＆咲戀', '安＆古蕾婭', '貪吃佩可(夏日)', '鈴莓(夏日)', 
        '凱留(夏日)', '珠希(夏日)', '忍(萬聖節)', '美咲(萬聖節)', '千歌(聖誕節)', '綾音(聖誕節)', '日和(新年)', '優衣(新年)', '靜流(情人節)', '鈴奈(夏日)', 
        '咲戀(夏日)', '真琴(夏日)', '真步(夏日)', '鏡華(萬聖節)', '克莉絲提娜(聖誕節)', '貪吃佩可(新年)', '可可蘿(新年)', '凱留(新年)', '流夏(夏日)', '初音(夏日)',  
        '紡希(萬聖節)', '秋乃(聖誕節)', '似似花(新年)', '可可蘿(祭服)', '惠理子(夏日)', '望(夏日)', '香織(萬聖節)', '宮子(聖誕節)', '雪菲(新年)', '伊莉亞(新年)',  
        '克蕾琪塔', '貪吃佩可(超載)', '凱留(超載)', '步未(怪盜)', '靜流(黑暗)', '伶(夏日)', '美美(夏日)', '涅婭', '智(萬聖節)','克莉絲提娜(狂野)',  
        '茜里(聖誕節)', '帆稀(新年)', '美里(新年)', '望(解放者)', '矛依未(解放者)'
        ]
    character_data = list(zip(character_names, getUplaoddata))

    for character, data in character_data:
        print(f"{character}，出現次數：{data}")

'''
# test n2c
name = 'C135'
code = convert_name_to_cardNumber(name)
if code:
    print(f"{name} 的编码是 {code}")
else:
    print(f"找不到 {name} 的编码")

name = '忍(萬聖節)'
code = convert_name_to_cardNumber(name)
if code:
    print(f"{name} 的编码是 {code}")
else:
    print(f"找不到 {name} 的编码")


# test c2n
name = '忍(萬聖節)'
code = convert_cardNumber_to_name(name)
if code:
    print(f"{name} 的编码是 {code}")
else:
    print(f"找不到 {name} 的编码")

name = 'C135'
code = convert_cardNumber_to_name(name)
if code:
    print(f"{name} 的编码是 {code}")
else:
    print(f"找不到 {name} 的编码")
'''