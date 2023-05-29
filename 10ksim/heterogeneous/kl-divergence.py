import numpy as np
from scipy.stats import entropy

# Input data (4 discrete probability distributions)
# grep -A 20 "statefreq" M4.txt | tail -n +2 | tr '\n' ' ' | sed -E "s/ +/,/g" | sed -e "s/^,/[/g" -e "s/,$/]/g"
distributions = np.array([
    [0.0015978725191777014,0.02751765899558606,0.0010937914008931284,0.0029000820747461823,0.0018127532522925996,0.014256448037638057,0.0020454060761162488,0.019822343718696886,0.002145576041929209,0.02025210518492668,0,0,0.0028629222487187938,0.0020486373653360217,0,0.009941061284631342,0.0038436185269198706,0.04306662272113328,0.0010954070455030148,0.02475167542346045,0.0012973626217388213,0.016570051118995458,0.004043958458545791,0.02404725437354996,0.001996936737819655,0.02119079470327071,0.004313771108396828,0.03099129490684193,0.007795485242702133,0.033275816385221375,0.007328563950444948,0.01657812934204489,0.006019891816436922,0.045981245597368436,0.0008255943956519772,0.028989511235192618,0.0024105417579505873,0.02619606170469894,0.0029049290085758415,0.022745044817981477,0.0023733819319231987,0.02562250786818925,0.007667849318521104,0.021879059307082338,0.0023749975765330854,0.009361044869682107,0.0006090980179271926,0.0005267001428229835,0.005724228852827701,0.05524535179045736,0.0019468517549131753,0.01637294247658931,0.004602971493566503,0.036767224387186,0.00874386862870548,0.031526073272714346,0.0112222674602713,0.0783636105133226,0.028498355273787135,0.0824899668469726,0.012899306565333437,0.046246211313389816,0.0060538203532445375,0.016326088782902603], #M1
    [0.02852953445159333,0.008582877223142167,0.01870789144366776,0.03457167776921035,0.011793555889825688,0.007230347233633755,0.008936810304508854,0.005119389212625299,0.02157727749617626,0.008595517690333834,0,0,0.005132029679816966,0.00233848643045847,0,0.009278102918683875,0.015636257916092577,0.007280909102400424,0.0033623642729835295,0.005536524629950323,0.007318830503975427,0.0032991619370251924,0.014738784745484193,0.011742994021059019,0.012994400273034092,0.007710684986917116,0.022386267396442974,0.009530912262517222,0.019883454892492828,0.01562361744890091,0.005688210236250332,0.0033750047401751968,0.04544247955404432,0.016002831464650934,0.008443832084033825,0.025356777186484814,0.01971912881900115,0.015206482031575886,0.011566027480375675,0.0077991682572587885,0.027695263616943282,0.012286534110300716,0.06442846127592876,0.016470528750742626,0.009720519270392233,0.005738772105017002,0.007862370593217125,0.0011376420472500664,0.027429813805918267,0.010529509170658948,0.019655926483042815,0.020136264236326175,0.024092730467318073,0.01899862218907611,0.012994400273034092,0.015471931842600902,0.04228236275612746,0.017368001921351014,0.07097622328121247,0.01553513417855924,0.03292841703429359,0.018606767706134418,0.01591434819430926,0.0057008507034419995],
    [0.01624791111152284,0.020041492131574627,0.021686869762982244,0.011472867738297978,0.014098163733859526,0.0062526408645515045,0.01067925738245483,0.005015905660212278,0.016820731037627528,0.013060088449984276,0,0,0.0035007377694196507,0.001968071336409989,0,0.007292774800452286,0.02592203164251096,0.007076101674764889,0.007394163412709809,0.009898513601771264,0.010947911471786946,0.0008502232865453195,0.0160698377113142,0.012490356501917892,0.010878946628931576,0.00894947501800034,0.02214183186062514,0.012969507760860805,0.030549366732903795,0.01406522530145099,0.0036556513343410433,0.0038810737311369575,0.032392374958762626,0.02860188191674914,0.0025156727752018893,0.027935907986489067,0.012918556123228852,0.005289191716601845,0.02293698620548744,0.01304207524476086,0.017272605157232123,0.021909718844746243,0.047264591854222736,0.01833023763534994,0.005228461481848608,0.006133239047070564,0.005269119859352894,0.0010298406757731139,0.030174692064256707,0.013280364216716358,0.024378557286367245,0.012064215532632466,0.02292309030431509,0.009941230631301083,0.02409806594788831,0.015864487171767236,0.03946333000346368,0.02532708120713179,0.06833026336850026,0.022965292670838525,0.033681605789752954,0.017393550963732213,0.018565438629267135,0.007600543278269538],
    [0.003970574287104988,0.0273937836201173,0.0004909149466403595,0.007987530134985977,0.004212383772498966,0.018191473505705973,0.001605635828661303,0.014875452480788132,0.0037329339307695273,0.02217872430904503,0,0,0.0013773760127075054,0.004057083715069213,0,0.010867877173288807,0.006696663550242695,0.0254243912811004,0.001804711741205483,0.04271741747469599,0.0047486379976506956,0.011456245511671998,0.005140014988018965,0.02843241789682031,0.0026109170728961795,0.016347676179576897,0.003098705172742651,0.03163274559036431,0.017392564149867683,0.03548971111062471,0.0022356954576296627,0.009920442594740852,0.0072996238403306955,0.04420475426632188,0.00039502497829447186,0.025744893077473883,0.004706946707065527,0.038719743848710644,0.0018948691570959098,0.01071101369246211,0.0038861494236700216,0.026137833491239097,0.005079041475538156,0.043556975838854824,0.0009198140985352808,0.00596289683594373,0.0001818782551777977,0.0007389781256221123,0.012787239963603503,0.035462090630612036,0.0030059420511906513,0.03018240981913276,0.015317901302123233,0.04177050403728035,0.01064430762752584,0.027635071964378963,0.017590597780147234,0.0529500236076933,0.017036624756496806,0.06228105558178633,0.02589393944131586,0.04971686402281347,0.00516086063331155,0.006333428181019414] # M4
])

# Compute KL divergence matrix
kl_divergence = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        kl_divergence[i, j] = 0.5*(entropy(distributions[i], distributions[j]) + entropy(distributions[j], distributions[i]))


print(kl_divergence)
