import psutil
import time

class Common(object):
    login = {"success":"1100", "1102":"token不存在或不能为空", "1103":"key不正确",
             "1104":"用户名或密码不能为空", "1105":"用户名或密码不正确"}

    citys = {'A': ['阿坝', '阿拉善', '阿里', '安康', '安庆', '鞍山', '安顺', '安阳', '澳门'],
             'B': ['北京', '白银', '保定', '宝鸡', '保山', '包头', '巴中', '北海', '蚌埠', '本溪', '毕节', '滨州',
                   '百色', '亳州'], 'C': ['重庆', '成都', '长沙', '长春', '沧州', '常德', '昌都', '长治', '常州',
                '巢湖', '潮州', '承德', '郴州', '赤峰', '池州', '崇左', '楚雄', '滁州', '朝阳'],
             'D': ['大连', '东莞', '大理', '丹东', '大庆', '大同', '大兴安岭', '德宏', '德阳', '德州', '定西', '迪庆',
                   '东营'], 'E': ['鄂尔多斯', '恩施', '鄂州'], 'F': ['福州', '防城港', '佛山', '抚顺', '抚州', '阜新',
            '阜阳'], 'G': ['广州', '桂林', '贵阳', '甘南', '赣州', '甘孜', '广安', '广元', '贵港', '果洛'],
             'H': ['杭州', '哈尔滨', '合肥', '海口', '呼和浩特', '海北', '海东', '海南', '海西', '邯郸', '汉中',
                   '鹤壁', '河池', '鹤岗', '黑河', '衡水', '衡阳', '河源', '贺州', '红河', '淮安', '淮北', '怀化',
                   '淮南', '黄冈', '黄南', '黄山', '黄石', '惠州', '葫芦岛', '呼伦贝尔', '湖州', '菏泽'],
             'J': ['济南', '佳木斯', '吉安', '江门', '焦作', '嘉兴', '嘉峪关', '揭阳', '吉林', '金昌', '晋城',
                   '景德镇', '荆门', '荆州', '金华', '济宁', '晋中', '锦州', '九江', '酒泉'], 'K': ['昆明', '开封'],
             'L': ['兰州', '拉萨', '来宾', '莱芜', '廊坊', '乐山', '凉山', '连云港', '聊城', '辽阳', '辽源', '丽江',
                   '临沧', '临汾', '临夏', '临沂', '林芝', '丽水', '六安', '六盘水', '柳州', '陇南', '龙岩', '娄底',
                   '漯河', '洛阳', '泸州', '吕梁'], 'M': ['马鞍山', '茂名', '眉山', '梅州', '绵阳', '牡丹江'],
             'N': ['南京', '南昌', '南宁', '宁波', '南充', '南平', '南通', '南阳', '那曲', '内江', '宁德', '怒江'],
             'P': ['盘锦', '攀枝花', '平顶山', '平凉', '萍乡', '莆田', '濮阳'], 'Q': ['青岛', '黔东南', '黔南',
            '黔西南', '庆阳', '清远', '秦皇岛', '钦州', '齐齐哈尔', '泉州', '曲靖', '衢州'], 'R': ['日喀则', '日照'],
             'S': ['上海', '深圳', '苏州', '沈阳', '石家庄', '三门峡', '三明', '三亚', '商洛', '商丘', '上饶', '山南',
                   '汕头', '汕尾', '韶关', '绍兴', '邵阳', '十堰', '朔州', '四平', '绥化', '遂宁', '随州', '宿迁',
                   '宿州'], 'T': ['天津', '太原', '泰安', '泰州', '台州', '唐山', '天水', '铁岭', '铜川', '通化',
                                '通辽', '铜陵', '铜仁', '台湾'], 'W': ['武汉', '乌鲁木齐', '无锡', '威海', '潍坊',
                '文山', '温州', '乌海', '芜湖', '乌兰察布', '武威', '梧州'], 'X': ['厦门', '西安', '西宁', '襄樊',
                '湘潭', '湘西', '咸宁', '咸阳', '孝感', '邢台', '新乡', '信阳', '新余', '忻州', '西双版纳', '宣城',
            '许昌', '徐州', '香港', '锡林郭勒', '兴安'], 'Y': ['银川', '雅安', '延安', '延边', '盐城', '阳江', '阳泉',
            '扬州', '烟台', '宜宾', '宜昌', '宜春', '营口', '益阳', '永州', '岳阳', '榆林', '运城', '云浮', '玉树',
            '玉溪', '玉林'], 'Z': ['杂多县', '赞皇县', '枣强县', '枣阳市', '枣庄', '泽库县', '增城市', '曾都区',
               '泽普县', '泽州县', '札达县', '扎赉特旗', '扎兰屯市', '扎鲁特旗', '扎囊县', '张北县',
               '张店区', '章贡区', '张家港', '张家界', '张家口', '漳平市', '漳浦县', '章丘市', '樟树市',
               '张湾区', '彰武县', '漳县', '张掖', '漳州', '长子县', '湛河区', '湛江', '站前区',
               '沾益县', '诏安县', '召陵区', '昭平县', '肇庆', '昭通', '赵县', '昭阳区', '招远市',
               '肇源县', '肇州县', '柞水县', '柘城县', '浙江', '镇安县', '振安区', '镇巴县', '正安县',
               '正定县', '正定新区', '正蓝旗', '正宁县', '蒸湘区', '正镶白旗', '正阳县', '郑州',
               '镇海区', '镇江', '浈江区', '镇康县', '镇赉县', '镇平县', '振兴区', '镇雄县', '镇原县',
               '志丹县', '治多县', '芝罘区', '枝江市', '芷江侗族自治县', '织金县', '中方县', '中江县',
               '钟楼区', '中牟县', '中宁县', '中山', '中山区', '钟山区', '钟山县', '中卫', '钟祥市',
               '中阳县', '中原区', '周村区', '周口', '周宁县', '舟曲县', '舟山', '周至县', '庄河市',
               '诸城市', '珠海', '珠晖区', '诸暨市', '驻马店', '准格尔旗', '涿鹿县', '卓尼', '涿州市',
               '卓资县', '珠山区', '竹山县', '竹溪县', '株洲', '株洲县', '淄博', '子长县', '淄川区',
               '自贡', '秭归县', '紫金县', '自流井区', '资溪县', '资兴市', '资阳']}

    data_source = {"腾讯房产": "dbhouse", "房天下": "", "透明售房": ""}

    areas = {
        '北京': ['朝阳', '大兴', '昌平', '房山', '通州', '海淀', '丰台', '顺义', '密云', '门头沟', '东城', '西城', '怀柔', '延庆', '石景山', '平谷', '大北京',
               '天津', '秦皇岛', '其它'],
        '潮州': ['饶平县', '枫溪区', '潮安区', '湘桥区'],
        '肇庆': ['端州', '鼎湖', '高要', '四会', '德庆', '广宁', '封开', '云浮', '怀集'],
        '汕尾': ['城区', '陆河县', '陆丰市', '海丰县'],
        '阳江': ['滨海新区', '江城区', '阳春市', '阳东区', '阳西县', '高新区', '海陵岛'],
        '汕头': ['南澳县', '澄海区', '潮南区', '潮阳区', '龙湖区', '濠江区', '金平区'],
        '茂名': ['茂南', '电白', '高州', '化州', '信宜'],
        '湛江': ['霞山区', '开发区', '赤坎区', '麻章区', '坡头区', '遂溪县', '徐闻县', '雷州市', '吴川市', '廉江市'],
        '清远': ['清城区', '清新区', '佛冈县', '连州市', '连山县', '连南县', '阳山县', '英德市'],
        '佛山': ['禅城', '南海', '顺德', '高明', '三水', '其他'],
        '惠州': ['龙门县', '其他', '惠城区', '惠阳区', '惠东县', '仲恺区', '博罗县', '大亚湾区'],
        '东莞': ['石碣', '常平', '黄江', '横沥', '中堂', '道滘', '石排', '企石', '望牛墩', '高埗', '麻涌', '茶山', '洪梅', '樟木头', '东坑', '谢岗', '桥头',
               '清溪', '塘厦', '石龙', '万江', '惠州', '凤岗', '大朗', '松山湖', '长安', '沙田', '莞城', '大岭山', '虎门', '厚街', '南城', '寮步', '东城',
               '其它'],
        '珠海': ['香洲', '斗门', '金湾', '横琴', '其他'],
        '中山': ['石岐区', '东区', '南区', '西区', '港口镇', '火炬区', '沙溪镇', '三角镇', '南朗镇', '东凤镇', '坦洲镇', '三乡镇', '民众镇', '古镇镇', '黄圃镇',
               '大涌镇', '神湾镇', '小榄镇', '横栏镇', '五桂山镇', '东升镇', '板芙镇', '阜沙镇', '南头镇'],
        '深圳': ['宝安', '龙岗', '龙华', '南山', '福田', '罗湖', '坪山', '光明', '盐田', '大鹏', '其他'],
        '江门': ['江海区', '新会区', '台山市', '开平市', '恩平市', '鹤山市', '蓬江区', '其他'],
        '三亚': ['待定', '崖州区', '海棠区', '天涯区', '吉阳区'],
        '宁德': ['福鼎市', '福安市', '霞浦县', '东侨区', '蕉城区', '罗源县', '柘荣县', '屏南县', '寿宁县', '周宁县', '古田县'],
        '莆田': ['涵江区', '秀屿区', '仙游县', '荔城区', '城厢区'],
        '海外地产': ['悉尼', '墨尔本', '布里斯班', '西班牙', '葡萄牙', '美国'],
        '泉州': ['丰泽区', '鲤城区', '洛江区', '台商投资区', '泉港区', '经济技术开发区', '晋江市', '南安市', '惠安县', '石狮市', '安溪县', '永春县', '德化县'],
        '福州': ['其他', '罗源县', '永泰县', '连江县', '长乐市', '福清市', '平潭县', '闽侯县', '马尾', '晋安', '仓山', '台江', '鼓楼', '闽清县'],
        '厦门': ['思明', '湖里', '集美', '海沧', '翔安', '同安', '漳州', '龙岩市', '泉州', '其他'],
        '渭南': [],
        '汉中': ['汉台区', '南郑', '城固', '洋县', '勉县', '西乡', '宁强', '略阳', '镇巴', '佛坪', '留坝'],
        '咸阳': ['西咸新区', '杨凌区', '淳化县', '旬邑县', '长武县', '彬县', '永寿县', '礼泉', '乾县', '泾阳县', '三原县', '武功县', '兴平市', '渭城区', '秦都区'],
        '西宁': ['经济技术开发区', '互助县', '湟源县', '湟中县', '大通县', '城南区', '城北区', '城东区', '城中区', '城西区', '海湖新区', '平安县'],
        '西安': ['城内', '城东', '城南', '城西', '城北', '高新', '曲江', '浐灞', '长安', '泾渭新区', '咸阳', '西咸新区', '周边'],
        '景德镇': ['鄱阳新行政中心', '乐平市', '浮梁县', '珠山区', '昌江区'],
        '鹰潭': ['其他', '月湖区', '龙虎山', '高新区', '信江区', '余江县', '贵溪市'],
        '抚州': ['抚州市区', '金巢区', '临川区', '广昌县', '资溪县', '宜黄县', '乐安县', '崇仁县', '南丰县', '黎川县', '南城县', '金溪县', '东乡县'],
        '新余': ['新余高新开发区', '仙女湖风景名胜区', '分宜县', '渝水区'],
        '上饶': ['上饶县', '信州区', '德兴市', '婺源县', '万年县', '鄱阳县', '余干县', '戈阳县', '横峰县', '铅山县', '玉山县', '广丰县'],
        '宜春': ['樟树', '丰城', '高安', '明月山', '经济开发区', '袁州区', '铜鼓县', '靖安', '奉新', '宜丰', '上高县', '万载县'],
        '赣州': ['安远县', '崇义县', '大余县', '定南县', '宁都县', '全南县', '瑞金市', '石城县', '寻乌县', '南昌', '龙南县', '会昌县', '南康区', '赣县', '信丰县',
               '兴国县', '于都县', '上犹县', '水东区', '水西区', '站北区', '开发区', '老城区', '章江新区'],
        '九江': ['浔阳区', '开发区', '庐山区', '共青城市', '瑞昌市', '修水县', '武宁县', '永修县', '德安县', '星子县', '都昌县', '彭泽县', '湖口县', '九江县', '南昌',
               '其它'],
        '吉安': ['城北区', '城南区', '青原区', '吉安县', '井冈山', '永丰县', '永新县', '吉水县', '市中心', '井开区', '安福县', '泰和县', '其他'],
        '池州': ['经开区', '东至', '石台', '青阳', '江南产业集中区', '站前区', '贵池区'],
        '滁州': ['南谯区', '琅琊区', '全椒县', '来安县', '定远县', '明光市', '天长市', '凤阳县', '新区'],
        '亳州': ['利辛县', '蒙城县', '涡阳县', '谯城区'],
        '淮北': ['相山区', '烈山区', '杜集区', '濉溪县'],
        '宣城': ['宣州区', '宁国市', '广德县', '郎溪县', '泾县', '旌德县', '绩溪县'],
        '铜陵': ['铜陵县', '郊区', '狮子山区', '铜官山区', '经开区'],
        '宝鸡': ['凤翔县', '岐山县', '陈仓区', '高新区', '金台区', '渭滨区', '陇县', '眉县', '太白县'],
        '宿州': ['老城区', '政务新区', '西南新区', '东关区', '经济开发区', '汴北高新区', '宿马新区', '灵璧县', '泗县', '萧县', '砀山县'],
        '六安': ['经开区', '裕安区', '金安区', '六安', '叶集试验区', '寿县', '金寨县', '霍邱县', '霍山县', '舒城县'],
        '阜阳': ['颍上县', '界首市', '太和县', '阜南县', '临泉县', '开发区', '颍泉区', '颍东区', '颍州区'],
        '马鞍山': ['开发区', '博望镇', '当涂县', '和县', '含山县', '秀山新区', '雨山区', '花山区'],
        '芜湖': ['繁昌县', '芜湖县', '南陵县', '无为县', '三山区', '开发区', '弋江区', '鸠江区', '镜湖区'],
        '淮南': ['凤台县', '毛集', '潘集', '大通', '八公山', '谢家集', '山南', '田家庵', '经开区'],
        '安庆': ['迎江区', '大观区', '宜秀区', '开发区', '桐城市', '怀宁县', '潜山县', '枞阳县', '太湖县', '宿松县', '望江县', '岳西县'],
        '蚌埠': ['固镇县', '五河县', '怀远县', '经开区', '高新区', '淮上区', '禹会区', '蚌山区', '龙子湖区'],
        '聊城': ['水城旅游度假区', '高新区', '开发区', '东昌府区', '嘉明开发区', '冠县', '阳谷', '高唐', '茌平', '东阿', '莘县', '临清'],
        '德州': ['宁津县', '陵城区', '乐陵市', '夏津县', '运河经济开发区', '经济开发区', '德城区'],
        '泰安': ['泰山区', '岱岳区', '高新区', '新泰市', '肥城市', '宁阳县', '东平县'],
        '菏泽': ['菏泽开发区', '牡丹区', '单县', '成武', '巨野', '东明', '鄄城', '郓城', '定陶', '曹县'],
        '潍坊': ['奎文区', '潍城区', '高新区', '坊子区', '寒亭区', '经开区', '滨海区', '诸城市', '青州市', '昌邑市', '高密市', '安丘市', '寿光市', '昌乐县', '临朐县',
               '峡山区'],
        '东营': ['河口', '东营港', '利津县', '垦利县', '广饶县', '新区', '西城', '东城'],
        '威海': ['乳山市', '荣成市', '南海新区', '文登区', '临港区', '高区', '经区', '环翠区'],
        '怒江': ['怒江'],
        '德宏州': ['芒市', '陇川县', '盈江县', '梁河县', '潞西市', '瑞丽市'],
        '迪庆': ['迪庆'],
        '临沧': ['临沧'],
        '玉溪': ['元江县', '新平县', '峨山县', '易门县', '华宁县', '通海县', '澄江县', '江川县', '红塔区'],
        '黄山': ['徽州区', '歙县', '休宁县', '祁门县', '黟县', '黄山区', '屯溪区'],
        '保山': ['隆阳区', '腾冲县', '昌宁县', '施甸县', '龙陵县'],
        '曲靖': ['市中心', '东片区', '南片区', '西片区', '北片区', '陆良县', '师宗县', '马龙县', '会泽县', '富源县', '罗平县', '沾益县', '宣威市'],
        '葫芦岛': ['龙港区', '连山区', '兴城市', '滨城区', '南票区', '绥中县', '建昌县', '龙湾中央商务区', '打渔山经济开发区', '东戴河新区'],
        '丽江': ['华坪县', '宁蒗县', '永胜县', '玉龙县', '古城区'],
        '朝阳': ['建平县', '喀喇沁左翼蒙古族自治县', '凌源市', '开发区', '北票', '朝阳县', '龙城区', '双塔区'],
        '丹东': ['其它', '凤城市', '宽甸满族自治县', '东港市', '振安区', '新城区', '元宝区', '振兴区'],
        '锦州': ['凌河区', '古塔区', '太和区', '松山新区', '开发区', '龙栖湾新区', '凌海市', '北镇市', '黑山市', '义县', '其他商圈'],
        '盘锦': ['兴隆台区', '双台子区', '大洼县', '盘山县', '田家镇', '辽东湾新区'],
        '辽阳': ['灯塔市', '弓长岭区', '文圣区', '辽阳县', '宏伟区', '白塔区', '太子河区'],
        '铁岭': ['其它区域', '昌图县', '西丰县', '开原市', '清河区', '铁岭县', '调兵山市', '新城区', '银州区'],
        '本溪': ['平山区', '明山区', '南芬区', '溪湖区', '本溪满族自治县', '桓仁满族自治县', '高新技术产业开发区'],
        '鞍山': ['其它', '岫岩县', '台安县', '海城市', '高新区', '千山区', '立山区', '铁西区', '铁东区'],
        '抚顺': ['其它区域', '抚顺县', '沈抚新区', '东洲区', '望花区', '顺城区', '新抚区'],
        '营口': ['其他区域', '沿海产业基地', '大石桥市', '盖州市', '鲅鱼圈区', '老边区', '西市区', '站前区'],
        '沈阳': ['沈河区', '皇姑区', '大东区', '浑南区', '沈北区', '铁西区', '和平区', '于洪区', '苏家屯', '其他区域'],
        '大连': ['普湾新区', '瓦房店', '普兰店', '长兴岛', '金州', '金州新区', '旅顺口区', '开发区', '高新区', '甘井子区', '沙河口区', '西岗区', '中山区', '其他',
               '长海县', '庄河', '北三市'],
        '舟山': ['定海区', '临城新区', '普陀区', '岱山县', '嵊泗县'],
        '嘉兴': ['南湖区', '秀洲区', '海宁市', '桐乡市', '嘉善县', '平湖市', '海盐县', '经开区'],
        '丽水': ['莲都区', '缙云', '青田', '遂昌', '云和', '松阳', '龙泉', '景宁', '庆元'],
        '湖州': ['其他', '吴兴区', '南浔区', '长兴县', '安吉县', '德清县'],
        '吉林': ['其他', '桦甸市', '蛟河市', '磬石市', '舒兰市', '永吉县', '经济技术开发区', '高新技术开发区', '龙潭区', '丰满区', '昌邑区', '船营区'],
        '金华': ['衢州市', '磐安县', '武义县', '浦江县', '兰溪市', '永康市', '东阳市', '义乌市', '金东区', '婺城区', '金西开发区'],
        '台州': ['椒江区', '黄岩区', '路桥区', '温岭市', '临海市', '玉环县', '天台县', '仙居县', '三门县', '开发区'],
        '温州': ['泰顺县', '文成县', '苍南县', '平阳县', '洞头县', '永嘉县', '乐清市', '瑞安市', '龙湾区', '瓯海区', '鹿城区'],
        '运城': ['永济市', '河津市', '绛县', '夏县', '新绛县', '稷山县', '芮城县', '万荣县', '临猗县', '闻喜县', '垣曲县', '平陆县', '盐湖区'],
        '晋城': ['金匠开发区', '晋城', '城区', '开发区', '泽州', '高平', '阳城', '陵川', '沁水县', '其他'],
        '宁波': ['海曙', '江东', '鄞州', '江北', '高新区', '镇海', '北仑', '东钱湖', '慈溪', '余姚', '奉化', '象山', '杭州湾', '宁海', '海外', '舟山'],
        '绍兴': ['越城区', '镜湖', '袍江', '高新', '柯桥区', '上虞区', '诸暨市', '嵊州市', '新昌县'],
        '杭州': ['西湖', '江干', '拱墅', '下城', '上城', '滨江', '下沙', '余杭', '萧山', '富阳', '临安', '建德', '淳安', '桐庐', '德清', '其他'],
        '临汾': ['尧都区', '曲沃县', '翼城县', '襄汾县', '洪洞县', '古\u3000县', '安泽县', '浮山县', '吉\u3000县', '乡宁县', '大宁县', '隰\u3000县', '永和县',
               '蒲\u3000县', '汾西县', '侯马市', '霍州市'],
        '朔州': ['怀仁县', '平鲁区', '山阴县', '应县', '右玉县', '开发区', '朔城区', '朔州'],
        '长治': ['长治市区', '郊  区', '高新开发区', '沁\u3000县', '武乡县', '长子县', '壶关县', '黎城县', '平顺县', '屯留县', '襄垣县', '长治县', '潞城市',
               '长治市'],
        '大同': ['大同', '云冈区', '新荣区', '左云县', '浑源县', '灵丘县', '天镇县', '阳高县', '广灵县', '大同县', '开发区', '矿区', '南郊区', '御东新区', '城区'],
        '张家口': ['桥东区', '桥西区', '高新区', '宣化县', '怀来县', '下花园区', '蔚县', '涿鹿县', '阳原县', '沽原县', '张北县', '尚义县', '赤城县', '崇礼县', '万全县',
                '康保县', '怀安县'],
        '承德': ['丰宁县', '宽城县', '围场县', '隆化县', '滦平县', '平泉县', '兴隆县', '承德县', '矿区', '开发区', '双滦区', '双桥区'],
        '唐山': ['路北区', '路南区', '开平区', '丰润区', '丰南区', '古冶区', '高新区', '迁安市', '滦县', '乐亭县', '滦南县', '迁西县', '玉田县', '遵化市', '曹妃甸新区',
               '海港开发区', '曹妃甸工业区', '南堡开发区', '汉沽管理区', '秦皇岛市', '其它', '海口市'],
        '宿迁': ['苏宿工业园区', '宿城区', '宿豫区', '经济开发区', '湖滨新城', '洋河新城', '泗洪县', '泗阳县', '沭阳县'],
        '连云港': ['灌南县', '灌云县', '赣榆区', '东海县', '海州区', '开发区', '连云区', '原新浦区'],
        '石家庄': ['长安区', '裕华区', '新华区', '桥西区', '高新区', '鹿泉区', '栾城区', '正定新区', '藁城区', '正定', '其他区', '平山', '辛集', '井陉', '井陉矿区',
                '灵寿', '元氏', '高邑', '赞皇', '无极', '新乐', '晋州', '赵县', '深泽'],
        '泰州': ['海陵区', '高港区', '姜堰区', '兴化市', '泰兴市', '靖江市'],
        '淮安': ['清河区', '清江浦区', '开发区', '新城', '淮安区', '淮阴区', '金湖县', '盱眙县', '洪泽县', '涟水县'],
        '盐城': ['城南', '河东', '城西南', '城中', '城西', '城北', '响水县', '滨海县', '建湖县', '东台市', '阜宁县', '射阳县', '大丰市'],
        '镇江': ['京口区', '润州区', '新区', '丹徒区'],
        '徐州': ['泉山区', '云龙区', '鼓楼区', '铜山区', '新城区', '金山桥', '贾汪区', '新沂市', '邳州市', '睢宁市', '沛县', '丰县'],
        '南通': ['崇川区', '港闸区', '开发区', '通州区', '启东市', '海门市', '如皋市', '海安县', '如东县', '其他'],
        '扬州': ['宝应县', '仪征市', '江都区', '邗江区', '广陵区', '高邮'],
        '漯河': ['郾城区', '源汇区', '召陵区', '西城区', '临颍县', '舞阳县'],
        '苏州': ['园区', '吴中', '新区', '相城', '吴江', '姑苏', '昆山', '太仓', '常熟', '张家港', '其他'],
        '周口': ['东区', '川汇区', '扶沟县', '鹿邑县', '太康县', '郸城县', '沈丘县', '商水县', '项城市', '淮阳县', '西华县'],
        '三门峡': ['高铁区', '渑池县', '湖滨区', '开发区', '灵宝市', '义马市', '卢氏县', '陕州区'],
        '无锡': ['宜兴市', '江阴市', '锡山区', '北塘区', '南长区', '崇安区', '惠山区', '滨湖区', '新区', '新吴区', '梁溪区'],
        '常州': ['天宁', '钟楼', '新北区', '武进区', '金坛', '溧阳'],
        '南京': ['海外', '都市圈', '江北', '城中', '城北', '城南', '河西', '仙林', '城东', '江宁'],
        '平顶山': ['新华区', '卫东区', '湛河区', '新城区', '高新区', '宝丰县', '石龙区', '鲁山县', '郏县', '叶县', '汝州市', '舞钢市', '海南省'],
        '南阳': ['宛城区', '卧龙区', '高新区', '宛东新区', '方城', '西峡', '新野', '桐柏', '唐河', '社旗', '淅川', '镇平', '油田', '内乡', '邓州', '麒麟湖景区',
               '南召', '鸭河工区'],
        '邵阳': ['其他区县', '邵东县', '北塔区', '双清区', '大祥区'],
        '开封': ['金明区', '顺河区', '龙亭区', '鼓楼区', '禹王台区', '开封县', '杞县', '通许县', '尉氏县', '兰考县'],
        '洛阳': ['吉利区', '伊滨区', '高新技术开发区', '瀍河回族区', '老城区', '洛龙区', '涧西区', '西工区', '伊川', '新安县', '洛宁', '汝阳', '栾川', '偃师', '宜阳',
               '经济技术开发区', '孟津', '嵩县'],
        '驻马店': ['驿城区', '开发区', '新蔡县', '平舆县', '西平县', '正阳县', '汝南县', '上蔡县', '遂平县', '泌阳县', '确山县'],
        '益阳': ['桃江县', '安化县', '大通湖区', '南县', '沅江', '高新区', '资阳区', '赫山区'],
        '郑州': ['郑州高新区', '二七区', '中原区', '新郑市', '金水区', '管城区', '郑东新区', '郑州经济技术开发区', '惠济区', '中牟县', '荥阳市', '郑上新区', '航空港区',
               '平原新区', '新密市', '许昌', '漯河', '驻马店', '平顶山', '南阳市', '洛阳', '汴西新城', '其他', '云南区', '巩义', '海南'],
        '永州': ['冷水滩区', '零陵区', '祁阳县', '东安县', '双牌县', '江华县', '江永县', '宁远县', '道县', '蓝山县', '新田县'],
        '常德': ['东营港', '广饶县', '利津县', '垦利县', '河口区', '新区', '西城区', '东城区', '津市市', '石门县', '桃源县', '安乡县', '澧县', '临澧县', '汉寿',
               '德山经济开发区', '鼎城区', '武陵区'],
        '岳阳': ['岳阳市', '岳阳县', '华容县', '平江县', '湘阴县', '临湘市', '汨罗市'],
        '湘潭': ['韶山市', '湘乡市', '九华区', '湘潭县', '岳塘区', '雨湖区'],
        '郴州': ['北湖区', '苏仙区', '武广新区', '汝城县', '宜章县', '资兴市', '临武县', '嘉禾县', '桂东县', '安仁县', '永兴县', '桂阳县'],
        '衡阳': ['蒸湘区', '石鼓区', '珠晖区', '雁峰区', '南岳区', '耒阳市', '常宁市', '衡南县', '衡阳县', '衡山县', '衡东县', '祁东县'],
        '株洲': ['芦淞区', '石峰区', '天元区', '荷塘区', '云龙区', '株洲县', '醴陵', '茶陵'],
        '长沙': ['岳麓区', '开福区', '雨花区', '芙蓉区', '天心区', '望城区', '长沙县', '宁乡市', '其它'],
        '许昌': ['东城区', '西城区', '南城区', 'CBD', '许东新城', '北海新区', '禹州市', '长葛市', '襄城县', '鄢陵县'],
        '孝感': ['开发东区', '老城区', '南城区', '南大片区', '北城区', '开发西区', '孝南乡镇', '孝昌', '汉川', '安陆', '云梦', '应城', '大悟'],
        '咸宁': ['温泉区', '赤壁市', '通山县', '崇阳县', '通城县', '嘉鱼县', '咸安区'],
        '随州': ['广水市', '乡镇', '随县', '曾都区'],
        '仙桃': ['乡镇', '老城区', '城东', '城南', '城西', '南城新区'],
        '荆门': ['漳河新区', '东宝区', '掇刀区', '高新区', '屈家岭', '钟祥市', '京山县'],
        '十堰': ['茅箭区', '张湾区', '白浪区', '郧西县', '郧阳区', '房县', '竹山县', '丹江口市', '竹溪县', '武当山'],
        '黄冈': ['黄州区', '团风县', '红安县', '罗田县', '英山县', '浠水县', '蕲春县', '黄梅县', '麻城市', '武穴市'],
        '鄂州': ['花湖开发区', '鄂城区', '华容区', '梁子湖区', '葛店开发区', '经济开发区'],
        '荆州': ['中心片区', '武德片区', '城南片区', '城东片区', '荆北新区', '沙北新区', '华中农高区', '江南新区', '海子湖片区', '岑河县', '关沮新城', '江陵县'],
        '黄石': ['黄石港区', '西塞山区', '下陆区', '铁山区', '大冶市', '阳新县', '花湖（鄂州）', '团城山开发区', '黄金山'],
        '恩施': ['舞阳坝', '六角亭', '小渡船', '航空路', '旗峰坝', '土桥坝', '金桂大道', '施州大道', '红庙开发区', '巴东县', '利川市', '鹤峰县', '咸丰县', '建始县',
               '宣恩县', '金龙大道', '来凤县'],
        '襄阳': ['樊城区', '襄城区', '高新区', '襄州区', '枣阳市', '南漳县', '宜城市', '老河口市', '东津新区', '谷城县', '保康县'],
        '宜昌': ['西陵区', '伍家区', '夷陵区', '开发区', '猇亭区', '当阳市', '远安县', '长阳县', '秭归县', '宜都市', '枝江市', '点军区', '其他'],
        '武汉': ['经济开发区', '东湖高新', '青山', '硚口', '黄陂', '江汉', '新洲', '汉南', '洪山', '东西湖', '汉阳', '其他', '武昌', '江岸', '江夏', '蔡甸'],
        '乐山': ['市中区', '井研县', '峨眉山市', '马边县', '峨边县', '沐川县', '夹江县', '犍为县', '金口河区', '沙湾区', '五通桥区'],
        '内江': ['市中区', '东兴区', '隆昌县', '资中县', '威远县'],
        '绵阳': ['经开区', '科创园区', '高新区', '游仙区', '涪城区', '海外置业', '仙海区', '北川县', '梓潼县', '盐亭县', '安州区', '平武县', '江油市', '三台县'],
        '自贡': ['自贡周边', '荣县', '富顺县', '沿滩区', '大安区', '贡井区', '自流井区'],
        '泸州': ['江阳区', '龙马潭', '纳溪区', '合江县', '叙永县', '泸县', '古蔺县', '四川甘孜州', '泸州周边'],
        '南充': ['达州市', '营山县', '西充县', '蓬安县', '阆中市', '高坪区', '顺庆区', '嘉陵区', '仪陇县', '南部县'],
        '云浮': ['高新区', '云安县', '郁南县', '罗定市', '新兴县', '云城区'],
        '韶关': ['南雄', '翁源县', '代管乐昌', '仁化县', '始兴县', '曲江区', '乳源瑶族自治县', '武江区', '浈江区', '新丰县'],
        '揭阳': ['普宁市', '惠来县', '揭西县', '揭东区', '榕城区'],
        '梅州': ['梅县区', '兴宁市', '梅江区', '大埔县', '平远县', '五华县', '丰顺县', '蕉岭县'],
        '广州': ['增城', '番禺', '花都', '南沙', '从化', '白云', '天河', '黄埔', '海珠', '荔湾', '越秀', '清远', '其他'],
        '成都': ['天府新区', '青羊区', '锦江区', '武侯区', '成华区', '金牛区', '高新区', '双流', '高新西区', '郫县', '龙泉驿', '新都', '温江', '都江堰', '大邑',
               '青白江', '金堂', '新津', '彭州', '崇州', '邛崃', '蒲江', '其他'],
        '天津': ['滨海新区', '滨海空港', '滨海汉沽', '滨海大港', '滨海塘沽', '宁河', '静海', '武清', '宝坻', '蓟州区', '北辰区', '东丽区', '西青区', '津南区', '河北区',
               '红桥区', '河东区', '河西区', '南开区', '和平区'],
        '重庆': ['两江新区', '大渡口', '北部新区', '九龙坡区', '渝中', '北碚', '沙坪坝', '巴南', '南岸', '渝北', '江北', '其他'],
        '上海': ['浦东', '嘉定', '松江', '宝山', '闵行', '普陀', '杨浦', '徐汇', '虹口', '长宁', '黄浦', '静安', '青浦', '金山', '奉贤', '崇明', '周边',
               '昆山']
             }



class PathHelp(object):
    tencent_path = "E:\\work2\\scrapy"
    tencent_result = "E:\\腾讯房产"






