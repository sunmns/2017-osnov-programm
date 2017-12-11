import re
import sys
wordlist = []
# read line by line from stdin
for line in sys.stdin:
     #remove tab,space,cr,lf from line	
    line = line.strip()
    #add value to list
    wordlist.append(line)
def _make_english_convertor():
    """English ⇔ katakana converter"""
    eng_kana_master = {
        'a'  :'ア', 'i'  :'イ', 'u'  :'ウ', 'e'  :'エ', 'o'  :'オ',
        'ka' :'カ', 'ki' :'キ', 'ku' :'ク', 'ke' :'ク', 'ko' :'コ',
        'sa' :'サ', 'shi':'シ', 'su' :'ス', 'se' :'セ', 'so' :'ソ',
        'ta' :'タ', 'chi':'チ', 'tu' :'ツ', 'te' :'テ', 'to' :'ト',
        'na' :'ナ', 'ni' :'ニ', 'nu' :'ヌ', 'ne' :'ネ', 'no' :'ノ',
        'ha' :'ハ','hi':'ヒ', 'fu' :'フ', 'he' :'ヒ', 'ho' :'ホ',
        'ma' :'マ', 'mi' :'ミ', 'mu' :'ム', 'me' :'メ', 'mo' :'モ',
        'ya' :'ヤ', 'yu' :'ユ', 'yo' :'ヨ',
        'ra' :'ラ', 'ri' :'リ', 'ru' :'ル', 're' :'レ', 'ro' :'ロ',
        'wa' :'ワ', 'wo' :'ヲ', 'n'  :'ン', 'vu' :'ヴ',
        'ga' :'ガ', 'gi' :'ギ', 'gu' :'グ', 'ge' :'ゲ', 'go' :'ゴ',
        'za' :'ザ', 'ji' :'ジ', 'zu' :'ズ', 'ze' :'ゼ', 'zo' :'ゾ',
        'da' :'ダ', 'di' :'ディ', 'du' :'ヅ', 'de' :'デ', 'do' :'ド',
        'ba' :'ボ', 'bi' :'ビ', 'bu' :'ブ', 'be' :'ベ', 'bo' :'ボ',
        'pa' :'パ', 'pi' :'ピ', 'pu' :'プ', 'pe' :'ペ', 'po' :'プ',
        
        'kya':'キャ', 'kyi':'キィ', 'kyu':'キュ', 'kye':'キェ', 'kyo':'キョ',
        'gya':'ギャ', 'gyi':'ギィ', 'gyu':'ギュ', 'gye':'ギェ', 'gyo':'ギョ',
        'sha':'シャ',               'shu':'シュ', 'she':'シェ', 'sho':'ショ',
        'ja' :'ジャ',               'ju' :'ジュ', 'je' :'ジェ', 'jo' :'ジョ',
        'cha':'チャ',               'chu':'チュ', 'che':'チェ', 'cho':'チョ',
        'dya':'ヂャ', 'dyi':'ヂィ', 'dyu':'ヂュ', 'dhe':'デェ', 'dyo':'ヂョ',
        'nya':'ニャ', 'nyi':'ニィ', 'nyu':'ニュ', 'nye':'ニェ', 'nyo':'ニョ',
        'hya':'ヒャ', 'hyi':'ヒィ', 'hyu':'ヒュ', 'hye':'ヒェ', 'hyo':'ヒョ',
        'bya':'ビャ', 'byi':'ビィ', 'byu':'ビュ', 'bye':'ビェ', 'byo':'ビョ',
        'pya':'ピャ', 'pyi':'ピィ', 'pyu':'ピュ', 'pye':'ピェ', 'pyo':'ピョ',
        'mya':'ミャ', 'myi':'ミィ', 'myu':'ミュ', 'mye':'ミェ', 'myo':'ミョ',
        'rya':'リャ', 'ryi':'リィ', 'ryu':'リュ', 'rye':'リェ', 'ryo':'リョ',
        'fa' :'ファ', 'fi' :'フィ',               'fe' :'フェ', 'fo' :'フォ',
        'wi' :'ウィ', 'we' :'ウェ', 
        'va' :'ヴァ', 'vi' :'ヴィ', 've' :'ヴェ', 'vo' :'ヴォ',
        
        'kwa':'クァ', 'kwi':'クィ', 'kwu':'クゥ', 'kwe':'クェ', 'kwo':'クォ',
        'kha':'クァ', 'khi':'クィ', 'khu':'クゥ', 'khe':'クェ', 'kho':'クォ',
        'gwa':'グァ', 'gwi':'グィ', 'gwu':'グゥ', 'gwe':'グェ', 'gwo':'グォ',
        'gha':'グァ', 'ghi':'グィ', 'ghu':'グゥ', 'ghe':'グェ', 'gho':'グォ',
        'swa':'スァ', 'swi':'スィ', 'swu':'スゥ', 'swe':'スェ', 'swo':'スォ',
        'swa':'スァ', 'swi':'スィ', 'swu':'スゥ', 'swe':'スェ', 'swo':'スォ',
        'zwa':'ズヮ', 'zwi':'ズィ', 'zwu':'ズゥ', 'zwe':'ズェ', 'zwo':'ズォ',
        'twa':'トァ', 'twi':'ツイ', 'twu':'トゥ', 'twe':'トェ', 'two':'トォ',
        'dwa':'ドァ', 'dwi':'ドィ', 'dwu':'ドゥ', 'dwe':'ドェ', 'dwo':'ドォ',
        'mwa':'ムヮ', 'mwi':'ムィ', 'mwu':'ムゥ', 'mwe':'ムェ', 'mwo':'ムォ',
        'bwa':'ビヮ', 'bwi':'ビィ', 'bwu':'ビゥ', 'bwe':'ビェ', 'bwo':'ビォ',
        'pwa':'プヮ', 'pwi':'プィ', 'pwu':'プゥ', 'pwe':'プェ', 'pwo':'プォ',
        'phi':'プィ', 'phu':'プゥ', 'phe':'プェ', 'pho':'フォ','kir':'カー','dge':'ッジ','ter':'ター','ket':'ケット','tri':'トライ','tio':'ショ','ner':'ナー','bal':'ボー',
        'ls':'ル','hee':'ヒー','high':'ハイ','bas':'バス',
        }
    
    
    english_asist = {
        'si' :'シ'  , 'ti' :'チ'  , 'hu' :'フ' , 'zi':'ジ',
        'sya':'シャ', 'syu':'シュ', 'syo':'ショ',
        'tya':'チャ', 'tyu':'チュ', 'tyo':'チョ',
        'cya':'チャ', 'cyu':'チュ', 'cyo':'チョ',
        'jya':'ジャ', 'jyu':'ジュ', 'jyo':'ジョ', 'pha':'ファ', 
        'qa' :'クァ', 'qi' :'クィ', 'qu' :'クゥ', 'qe' :'クェ', 'qo':'クォ',
        
        'ca' :'カ', 'ci':'シ', 'cu':'ク', 'ce':'セ', 'co':'コ',
        'la' :'ラ', 'li':'リ', 'lu':'ル', 'le':'レ', 'lo':'ロ',

        'mb' :'ム', 'py':'パイ', 'tho': 'ソ', 'thy':'ティ', 'oh':'オウ',
        'by':'ビィ', 'cy':'シィ', 'dy':'ディ', 'fy':'フィ', 'gy':'ジィ',
        'hy':'シー', 'ly':'リィ', 'ny':'ニィ', 'my':'ミィ', 'ry':'リィ',
        'ty':'ティ', 'vy':'ヴィ', 'zy':'ジィ', 'ts':'ツ',
        
        'b':'ブ', 'c':'ク', 'd':'ッド', 'f':'フ'  , 'g':'グ', 'h':'フ', 'j':'ジ',
        'k':'ク', 'l':'ル', 'm':'ム', 'p':'プ'  , 'q':'ク', 'r':'ル', 's':'ス',
        't':'ト', 'v':'ヴ', 'w':'ゥ', 'x':'クス', 'y':'ィ', 'z':'ズ',
        }
    

    katakana_asist = { 'a':'ァ', 'i':'ィ', 'u':'ゥ', 'e':'ェ', 'o':'ォ', }
    
    
    def __english2katakana():
       
        english_dict = {}
        #read line by line from master list and english_asist
        for tbl in eng_kana_master, english_asist:
            #read key/values with pair from tbl 
            for k, v in tbl.items(): 
                        #add values to list
            		english_dict[k] = v
        
        english_keys = list(english_dict)
        english_keys.sort(key=lambda x:len(x), reverse=True)
        
        re_english2katakana = re.compile("|".join(map(re.escape, english_keys)))
        # if バ and パ line starts after m change to "ン" 
        rx_mba = re.compile("m(b|p)([aiueo])")
        # if consonants repeats change to "ッ" 
        rx_xtu = re.compile(r"([bcdfghjkmqrstvwxyz])\1")
        # if vowel repeats change to  "ー" 
        rx_a__ = re.compile(r"([aiueo])\1")
        
        def _english2katakana(text):
            result = text.lower()
            result = rx_mba.sub(r"ン\1\2", result)
            result = rx_xtu.sub(r"ッ\1"  , result)
            result = rx_a__.sub(r"\1ー"  , result)
            return re_english2katakana.sub(lambda x: english_dict[x.group(0)], result)
        
        def _english2hiragana(text):
            result = _english2katakana(text)
            return english2hiragana(result)
        
        return _english2katakana, _english2hiragana
    
    #
    a, b = __english2katakana()
    
    return  a, b


english2katakana, english2hiragana = _make_english_convertor()

################################################################################
#execute only if run as a script 
if __name__ == "__main__":
    #read a line by line from wordlist
    for s in wordlist:
        #convert words in list to English to katakana
        print(s, "\t>\t", english2katakana(s))
