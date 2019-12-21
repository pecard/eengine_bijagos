import ee
from ee_plugin import Map

# images
bands1 = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']
names1 = ['B21', 'B31', 'B41', 'B51', 'B61', 'B71']

bands2 = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']
names2 = ['B22', 'B32', 'B42', 'B52', 'B62', 'B72']

all_bands = ['B21', 'B31', 'B41', 'B51', 'B61', 'B71', 'B22', 'B32', 'B42', 'B52', 'B62', 'B72']

# Filter image based on cloud cover (TOA)
image1 = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')\
  .filterBounds(roi)\
  .filterDate('2019-03-01', '2019-04-28')\
  .sort('CLOUD_COVER')\
  .first()\
  .select(bands1)\
  .rename(names1)

image2 = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')\
  .filterBounds(roi)\
  .filterDate('2019-05-01', '2019-07-28')\
  .sort('CLOUD_COVER')\
  .first()\
  .select(bands2)\
  .rename(names2)


# stack to create multi-date composite
stck = image1.addBands(image2)

# Define visualization parameters in a JavaScript dictionary for true colour rendering
# Bands 4,3 and 2 needed for RGB.
trueColour = {"bands": ["B41", "B31", "B21"], "min": 0, "max": 2000};
trueColour2 = {"bands": ["B42", "B32", "B22"], "min": 0, "max": 2000};

# ClassificationMode

mangal = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-15.645858585977521, 11.031324431662814]),
            {
              "landcover": 0,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.646180451059308, 11.031129615565991]),
            {
              "landcover": 0,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.63913160576817, 11.026469978844643]),
            {
              "landcover": 0,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.639002859735456, 11.025585392814264]),
            {
              "landcover": 0,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.638487875604596, 11.02590131670203]),
            {
              "landcover": 0,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.702415568344918, 11.01878376326881]),
            {
              "landcover": 0,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.702380699627724, 11.018562611231902]),
            {
              "landcover": 0,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.701694054119912, 11.017214633317662]),
            {
              "landcover": 0,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.700465398749884, 11.013418134526196]),
            {
              "landcover": 0,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.658295793656066, 10.963560860264012]),
            {
              "landcover": 0,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.658075852516845, 10.96357665978902]),
            {
              "landcover": 0,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.658038301590636, 10.963408131478793]),
            {
              "landcover": 0,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.657898826721862, 10.963476596116411]),
            {
              "landcover": 0,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.657802267197326, 10.963365999386236]),
            {
              "landcover": 0,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.756500653553076, 11.171444039714329]),
            {
              "landcover": 0,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.756833247470922, 11.171465090802261]),
            {
              "landcover": 0,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.75715511255271, 11.171444039714329]),
            {
              "landcover": 0,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.757814935970373, 11.172262399633102]),
            {
              "landcover": 0,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.75725435428626, 11.172401862668774]),
            {
              "landcover": 0,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.757844440269537, 11.171872955329407]),
            {
              "landcover": 0,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.749301604557104, 11.17377806978401]),
            {
              "landcover": 0,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.749569825458593, 11.173849116628022]),
            {
              "landcover": 0,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.750964574146337, 11.173630713311338]),
            {
              "landcover": 0,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.751956991481848, 11.173878061633559]),
            {
              "landcover": 0,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.99549296649434, 11.034935048367318]),
            {
              "landcover": 0,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.99598649295308, 11.035777484515352]),
            {
              "landcover": 0,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.996909172854203, 11.036219762526036]),
            {
              "landcover": 0,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.001136334261673, 11.034850804619655]),
            {
              "landcover": 0,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.988030561313167, 11.059524281089686]),
            {
              "landcover": 0,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.988545545444026, 11.059945464173406]),
            {
              "landcover": 0,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.990262159213557, 11.059418985224204]),
            {
              "landcover": 0,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.13709430488666, 12.346748805556881]),
            {
              "landcover": 0,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.130142019120058, 12.348006485750492]),
            {
              "landcover": 0,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.127652929154237, 12.34393996464039]),
            {
              "landcover": 0,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.12735252174457, 12.346036117431405]),
            {
              "landcover": 0,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.126150892105898, 12.347629182326946]),
            {
              "landcover": 0,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.14683608802875, 12.343269192202708]),
            {
              "landcover": 0,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.148466871109804, 12.345826502907581]),
            {
              "landcover": 0,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.149711416092714, 12.339621836999477]),
            {
              "landcover": 0,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.116409108963808, 12.356474708346648]),
            {
              "landcover": 0,
              "system:index": "39"
            })])

palmar = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-15.639067232751813, 11.029076332925566]),
            {
              "landcover": 1,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.638477146768537, 11.029281681052996]),
            {
              "landcover": 1,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.634539663934675, 11.02893416875332]),
            {
              "landcover": 1,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.635199487352338, 11.028423430234014]),
            {
              "landcover": 1,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.635499894762006, 11.028386572780754]),
            {
              "landcover": 1,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.635843217515912, 11.028344449971383]),
            {
              "landcover": 1,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.641074715571676, 11.03069820992793]),
            {
              "landcover": 1,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.641375122981344, 11.03089829161655]),
            {
              "landcover": 1,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.640393434481894, 11.030129555964]),
            {
              "landcover": 1,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.632373629527365, 11.031503801160163]),
            {
              "landcover": 1,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.632373629527365, 11.03193555502938]),
            {
              "landcover": 1,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.64071529956368, 11.034847244437007]),
            {
              "landcover": 1,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.640892325358664, 11.03469455258097]),
            {
              "landcover": 1,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.644110976176535, 11.034520799682726]),
            {
              "landcover": 1,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.624672455106747, 11.05009472285633]),
            {
              "landcover": 1,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.624296945844662, 11.050131577585327]),
            {
              "landcover": 1,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.623717588697446, 11.05020528702942]),
            {
              "landcover": 1,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.641404074941647, 11.049147028235042]),
            {
              "landcover": 1,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62584726265527, 11.051000294856562]),
            {
              "landcover": 1,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.706656140797463, 11.01758058886984]),
            {
              "landcover": 1,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.706513983719674, 11.017593752730148]),
            {
              "landcover": 1,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.708402258866158, 11.01745684855421]),
            {
              "landcover": 1,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.707321328633157, 11.017246226620694]),
            {
              "landcover": 1,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.710531932823983, 11.017667470336967]),
            {
              "landcover": 1,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.710757238381234, 11.01783070211492]),
            {
              "landcover": 1,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.711073739044991, 11.018009730412441]),
            {
              "landcover": 1,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.704338508567389, 11.013376009573552]),
            {
              "landcover": 1,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.703909355125006, 11.013333884614875]),
            {
              "landcover": 1,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.672489113997017, 10.971389520454418]),
            {
              "landcover": 1,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.67366928596357, 10.971663371516906]),
            {
              "landcover": 1,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.673926778029, 10.972137343910001]),
            {
              "landcover": 1,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.674516864012276, 10.971852960565348]),
            {
              "landcover": 1,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.671573193960057, 10.980969658882072]),
            {
              "landcover": 1,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.670897277288304, 10.981080249024492]),
            {
              "landcover": 1,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.671192320279943, 10.982333601077233]),
            {
              "landcover": 1,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.671358617238866, 10.983155123065519]),
            {
              "landcover": 1,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.667608889036046, 10.988015748047472]),
            {
              "landcover": 1,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.67275873034464, 11.001654560608387]),
            {
              "landcover": 1,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.625981005124913, 11.042704100924412]),
            {
              "landcover": 1,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.617998751096593, 11.043504394151652]),
            {
              "landcover": 1,
              "system:index": "39"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.614694269590245, 11.045989501319339]),
            {
              "landcover": 1,
              "system:index": "40"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.615852983884679, 11.046221162779815]),
            {
              "landcover": 1,
              "system:index": "41"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.620144518308507, 11.045736779517538]),
            {
              "landcover": 1,
              "system:index": "42"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.631012829236852, 11.041503656993301]),
            {
              "landcover": 1,
              "system:index": "43"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.627955110959874, 11.042325013897466]),
            {
              "landcover": 1,
              "system:index": "44"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.642138632230626, 11.039313360683343]),
            {
              "landcover": 1,
              "system:index": "45"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.643125685148107, 11.040492753034119]),
            {
              "landcover": 1,
              "system:index": "46"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.728218548345126, 11.185569139878735]),
            {
              "landcover": 1,
              "system:index": "47"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.729972713040866, 11.185558614846965]),
            {
              "landcover": 1,
              "system:index": "48"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.729076855229891, 11.185474414579076]),
            {
              "landcover": 1,
              "system:index": "49"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.734226696538485, 11.184442959311651]),
            {
              "landcover": 1,
              "system:index": "50"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.731667869138278, 11.184700823472708]),
            {
              "landcover": 1,
              "system:index": "51"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.730707638310946, 11.184500847204516]),
            {
              "landcover": 1,
              "system:index": "52"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.751438754446667, 11.18560559510045]),
            {
              "landcover": 1,
              "system:index": "53"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.863486755636586, 11.243322129392935]),
            {
              "landcover": 1,
              "system:index": "54"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.863438475874318, 11.243543110803834]),
            {
              "landcover": 1,
              "system:index": "55"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.863513577726735, 11.243132716620156]),
            {
              "landcover": 1,
              "system:index": "56"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.865798819807424, 11.243085363407504]),
            {
              "landcover": 1,
              "system:index": "57"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.862440694120778, 11.243511542041226]),
            {
              "landcover": 1,
              "system:index": "58"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.869210589674367, 11.243216900090086]),
            {
              "landcover": 1,
              "system:index": "59"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.849850405004872, 11.250951151464292]),
            {
              "landcover": 1,
              "system:index": "60"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.850016701963796, 11.250840663620892]),
            {
              "landcover": 1,
              "system:index": "61"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.06920360203094, 11.934475809526601]),
            {
              "landcover": 1,
              "system:index": "62"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.069525467112726, 11.935084630747399]),
            {
              "landcover": 1,
              "system:index": "63"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.068345295146173, 11.934895686376931]),
            {
              "landcover": 1,
              "system:index": "64"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.068817363932794, 11.935693450600771]),
            {
              "landcover": 1,
              "system:index": "65"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.06888173694915, 11.935084630747399]),
            {
              "landcover": 1,
              "system:index": "66"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.06446145649261, 11.934769723390126]),
            {
              "landcover": 1,
              "system:index": "67"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.06463848228759, 11.934921928658497]),
            {
              "landcover": 1,
              "system:index": "68"
            })])

dunar = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-15.627306384359372, 11.05204275218642]),
            {
              "landcover": 2,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.626684111867917, 11.052053282039529]),
            {
              "landcover": 2,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.626212043081296, 11.052242819331049]),
            {
              "landcover": 2,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.623207968984616, 11.052527125038715]),
            {
              "landcover": 2,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.621952695165646, 11.05196904320398]),
            {
              "landcover": 2,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.625257176671994, 11.052706132194755]),
            {
              "landcover": 2,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.628904980932248, 11.051600498014054]),
            {
              "landcover": 2,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62858311585046, 11.051674207089087]),
            {
              "landcover": 2,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.628679675374997, 11.0515057291761]),
            {
              "landcover": 2,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.643603486333859, 11.051000294856562]),
            {
              "landcover": 2,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.627123994146359, 11.05182162518358]),
            {
              "landcover": 2,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.71259723376545, 11.017040870090378]),
            {
              "landcover": 2,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.712763530724374, 11.017319944314558]),
            {
              "landcover": 2,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.712908370011178, 11.017577956097714]),
            {
              "landcover": 2,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.713466269486275, 11.018999649620723]),
            {
              "landcover": 2,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.708164131051035, 11.005461476118164]),
            {
              "landcover": 2,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.707756435280771, 11.005693169509705]),
            {
              "landcover": 2,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.708357250100107, 11.005782687362181]),
            {
              "landcover": 2,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.884405214739218, 11.055893430888414]),
            {
              "landcover": 2,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.884952385378256, 11.05559859871854]),
            {
              "landcover": 2,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.946955997407258, 11.046897507290236]),
            {
              "landcover": 2,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.02343085559346, 11.032091808535153]),
            {
              "landcover": 2,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.020641358217972, 11.031796952459684]),
            {
              "landcover": 2,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.007552178225296, 11.03322910776935]),
            {
              "landcover": 2,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.00544932635762, 11.033481840334746]),
            {
              "landcover": 2,
              "system:index": "24"
            })])

agua = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-15.610022229467404, 11.04655664732007]),
            {
              "landcover": 3,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.611288232122433, 11.046177565268303]),
            {
              "landcover": 3,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.611567181859982, 11.045082436590663]),
            {
              "landcover": 3,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.609721822057736, 11.0447244128675]),
            {
              "landcover": 3,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.60714690140344, 11.044829714007884]),
            {
              "landcover": 3,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.605347387186157, 11.053759316401303]),
            {
              "landcover": 3,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.643027059427368, 11.056286455517407]),
            {
              "landcover": 3,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.648176900735962, 11.047946813805124]),
            {
              "landcover": 3,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.648691884866821, 11.0408705682964]),
            {
              "landcover": 3,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.652039281717407, 11.03421537227077]),
            {
              "landcover": 3,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.646116964212524, 11.027475779638216]),
            {
              "landcover": 3,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.629809133401977, 11.026043596297317]),
            {
              "landcover": 3,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.618651143900024, 11.031940777035016]),
            {
              "landcover": 3,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.610153905740844, 11.03817481086044]),
            {
              "landcover": 3,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.605862307566895, 11.042378836954596]),
            {
              "landcover": 3,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.603802371043457, 11.042041870359277]),
            {
              "landcover": 3,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.601399111766113, 11.033617579819982]),
            {
              "landcover": 3,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.679247546214356, 11.035470944467825]),
            {
              "landcover": 3,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.675556826609863, 11.031006000702378]),
            {
              "landcover": 3,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.647833514231934, 11.037324297423877]),
            {
              "landcover": 3,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.646803545970215, 11.036481865711545]),
            {
              "landcover": 3,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.648863482493653, 11.034796995039466]),
            {
              "landcover": 3,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.622685122508301, 11.030921755828329]),
            {
              "landcover": 3,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.606892275828613, 11.028310152756644]),
            {
              "landcover": 3,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62594668867041, 11.05830006754331]),
            {
              "landcover": 3,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62423007490088, 11.05830006754331]),
            {
              "landcover": 3,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.200845048752626, 12.345931310190478]),
            {
              "landcover": 3,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.210801408615907, 12.335534223396483]),
            {
              "landcover": 3,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.16256456169208, 12.330838629578919]),
            {
              "landcover": 3,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.1390469530495, 12.323459669342972]),
            {
              "landcover": 3,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.097504899826845, 12.334695730671573]),
            {
              "landcover": 3,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.125228212204775, 12.350333178176125]),
            {
              "landcover": 3,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.137652204361757, 12.347964563174733]),
            {
              "landcover": 3,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.13286714347919, 12.346350538902424]),
            {
              "landcover": 3,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.157908246842226, 12.348299943592778]),
            {
              "landcover": 3,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.161684797135194, 12.3542528744865]),
            {
              "landcover": 3,
              "system:index": "35"
            })])

pradohumido = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-15.706870513877448, 11.020284421225975]),
            {
              "landcover": 4,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.707610803565558, 11.020789908393674]),
            {
              "landcover": 4,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.708469110450324, 11.021337518511894]),
            {
              "landcover": 4,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.709091382941779, 11.021779818247829]),
            {
              "landcover": 4,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.708426195106085, 11.022085215296418]),
            {
              "landcover": 4,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.706773954352911, 11.020021146315486]),
            {
              "landcover": 4,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.706173139533576, 11.01932609941986]),
            {
              "landcover": 4,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.705658155402716, 11.019515657826954]),
            {
              "landcover": 4,
              "system:index": "7"
            })])

secundario = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-15.623218166568222, 11.04233050735248]),
            {
              "landcover": 5,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.633045780398788, 11.041614452757324]),
            {
              "landcover": 5,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.636564838626327, 11.042246265726057]),
            {
              "landcover": 5,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.635878193118515, 11.041024759426591]),
            {
              "landcover": 5,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.635620701053085, 11.039550520918805]),
            {
              "landcover": 5,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.622488605716171, 11.038371124784124]),
            {
              "landcover": 5,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.621673214175644, 11.038623852925966]),
            {
              "landcover": 5,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.616169321277084, 11.052028662982696]),
            {
              "landcover": 5,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.635942566134872, 11.034158957074771]),
            {
              "landcover": 5,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.669373619296493, 10.970632159239138]),
            {
              "landcover": 5,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.664824592807236, 10.974002624833366]),
            {
              "landcover": 5,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.661305534579697, 10.972738704740314]),
            {
              "landcover": 5,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.66147719595665, 10.971137731528769]),
            {
              "landcover": 5,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.665682899692001, 10.968525598724367]),
            {
              "landcover": 5,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.668858635165634, 10.97037937277003]),
            {
              "landcover": 5,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.670017349460068, 10.970842814464904]),
            {
              "landcover": 5,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.630968413934056, 11.049601935919359]),
            {
              "landcover": 5,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.632212958916966, 11.050907645687547]),
            {
              "landcover": 5,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.632985435113255, 11.050065252953866]),
            {
              "landcover": 5,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.629080138787572, 11.048928018926778]),
            {
              "landcover": 5,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.633457503899876, 11.049433456816335]),
            {
              "landcover": 5,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.634744964227025, 11.048759539436785]),
            {
              "landcover": 5,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.638650260552708, 11.052171230252627]),
            {
              "landcover": 5,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.639465652093236, 11.052845139795087]),
            {
              "landcover": 5,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.639251075372044, 11.054108716013896]),
            {
              "landcover": 5,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.638821921929662, 11.054108716013896]),
            {
              "landcover": 5,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.664969129685119, 10.96686820909263]),
            {
              "landcover": 5,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.664840383652404, 10.966362629501205]),
            {
              "landcover": 5,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.664754552963927, 10.965941312514673]),
            {
              "landcover": 5,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.663724584702209, 10.966025575960007]),
            {
              "landcover": 5,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.663166685227111, 10.965941312514673]),
            {
              "landcover": 5,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.664883298996642, 10.965477863136138]),
            {
              "landcover": 5,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.665655775192931, 10.966404761166844]),
            {
              "landcover": 5,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.661235494736388, 10.970491504196845]),
            {
              "landcover": 5,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.66119257939215, 10.972513789128712]),
            {
              "landcover": 5,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.66170756352301, 10.97259805070057]),
            {
              "landcover": 5,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.661106748703673, 10.970238717607437]),
            {
              "landcover": 5,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.66544119847174, 10.966109839381332]),
            {
              "landcover": 5,
              "system:index": "37"
            })])

floresta = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-15.663740980365219, 10.971432648298332]),
            {
              "landcover": 6,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.621529216971794, 11.040488595004883]),
            {
              "landcover": 6,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62088548680822, 11.040499125272547]),
            {
              "landcover": 6,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.619855518546501, 11.040351701490929]),
            {
              "landcover": 6,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.619179601874748, 11.039825187380988]),
            {
              "landcover": 6,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.619791145530144, 11.03962511177171]),
            {
              "landcover": 6,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.619404907432, 11.039456626942362]),
            {
              "landcover": 6,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.622344608512321, 11.040857154148336]),
            {
              "landcover": 6,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62538086911718, 11.038572080002567]),
            {
              "landcover": 6,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.6263571931986, 11.038687913681988]),
            {
              "landcover": 6,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.626754160132805, 11.038561549665811]),
            {
              "landcover": 6,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62861024877111, 11.037856016242975]),
            {
              "landcover": 6,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.628567333426872, 11.038803747315724]),
            {
              "landcover": 6,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.6298869802622, 11.03795078948788]),
            {
              "landcover": 6,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62614261647741, 11.037898137688918]),
            {
              "landcover": 6,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.625649090018669, 11.038171926940354]),
            {
              "landcover": 6,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62586366673986, 11.038730035008623]),
            {
              "landcover": 6,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.620027179923454, 11.038993293163289]),
            {
              "landcover": 6,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62011301061193, 11.038814277643791]),
            {
              "landcover": 6,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.628476116973161, 11.040828185470678]),
            {
              "landcover": 6,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.628401015120744, 11.041270455875845]),
            {
              "landcover": 6,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.628304455596208, 11.040659701331592]),
            {
              "landcover": 6,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.628862355071306, 11.041007199762548]),
            {
              "landcover": 6,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.62825081141591, 11.041997041523869]),
            {
              "landcover": 6,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.639344427901506, 11.039575082372052]),
            {
              "landcover": 6,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.639666292983293, 11.039701445952138]),
            {
              "landcover": 6,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.639773581343889, 11.040122657493091]),
            {
              "landcover": 6,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.638121340590715, 11.040206899728796]),
            {
              "landcover": 6,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.638035509902238, 11.038732657115293]),
            {
              "landcover": 6,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.656820578697875, 10.963281735183118]),
            {
              "landcover": 6,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.6569332314765, 10.963513461683952]),
            {
              "landcover": 6,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.656659646156982, 10.963792586546152]),
            {
              "landcover": 6,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.656235857132629, 10.96342393101197]),
            {
              "landcover": 6,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.656064195755675, 10.963992713643714]),
            {
              "landcover": 6,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.655677957657531, 10.963487129136169]),
            {
              "landcover": 6,
              "system:index": "34"
            })])

cajual = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-16.099201728291405, 12.368189270925635]),
            {
              "landcover": 7,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.097957183308495, 12.367099365890462]),
            {
              "landcover": 7,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.096498061604393, 12.366051375992734]),
            {
              "landcover": 7,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.095124770588768, 12.36512914140631]),
            {
              "landcover": 7,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.094438125080956, 12.364584183075582]),
            {
              "landcover": 7,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.098386336750877, 12.363787703471377]),
            {
              "landcover": 7,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.100145865864647, 12.36475186268298]),
            {
              "landcover": 7,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.084481765217674, 12.36529682066408]),
            {
              "landcover": 7,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.084524680561913, 12.366051375992734]),
            {
              "landcover": 7,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.085168410725487, 12.370410986340614]),
            {
              "landcover": 7,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.086885024495018, 12.370830175809632]),
            {
              "landcover": 7,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.084996749348534, 12.372171577590082]),
            {
              "landcover": 7,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.103664924092186, 12.371710471505018]),
            {
              "landcover": 7,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.0988584055375, 12.373890238553784]),
            {
              "landcover": 7,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.09731345314492, 12.37498011525599]),
            {
              "landcover": 7,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.09705596107949, 12.376656839761932]),
            {
              "landcover": 7,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.140657950825585, 12.37263268286114]),
            {
              "landcover": 7,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.141344596333397, 12.374057912188634]),
            {
              "landcover": 7,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.159197379536522, 12.374057912188634]),
            {
              "landcover": 7,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.1387696756791, 12.35703848942322]),
            {
              "landcover": 7,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.13276152748574, 12.358379961988085]),
            {
              "landcover": 7,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.13404898781289, 12.364835702446344]),
            {
              "landcover": 7,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.130186606831444, 12.36475186268298]),
            {
              "landcover": 7,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.173101951069725, 12.400297508423849]),
            {
              "landcover": 7,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.1717286600541, 12.401345360796569]),
            {
              "landcover": 7,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.171556998677147, 12.400297508423849]),
            {
              "landcover": 7,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.173144866413963, 12.402141725781624]),
            {
              "landcover": 7,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.149627257771385, 12.403021915827953]),
            {
              "landcover": 7,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.147610236592186, 12.40490802734218]),
            {
              "landcover": 7,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.148597289509667, 12.405872034620241]),
            {
              "landcover": 7,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.840100423329773, 11.288543455297928]),
            {
              "landcover": 7,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.839842931264343, 11.288669710558857]),
            {
              "landcover": 7,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.840475932591858, 11.288006869819444]),
            {
              "landcover": 7,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.84266461514801, 11.287670188222766]),
            {
              "landcover": 7,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.13966453204864, 12.37890364865177]),
            {
              "landcover": 7,
              "system:index": "34"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.140286804540096, 12.379700082166007]),
            {
              "landcover": 7,
              "system:index": "35"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.139128090245663, 12.380517471930222]),
            {
              "landcover": 7,
              "system:index": "36"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.13841998706573, 12.379846793337796]),
            {
              "landcover": 7,
              "system:index": "37"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.14865529666656, 12.377855706115362]),
            {
              "landcover": 7,
              "system:index": "38"
            }),
        ee.Feature(
            ee.Geometry.Point([-16.14989984164947, 12.377981459441836]),
            {
              "landcover": 7,
              "system:index": "39"
            })])

povoacao = ee.FeatureCollection(
        [ee.Feature(
            ee.Geometry.Point([-15.873886619598466, 11.233242784071711]),
            {
              "landcover": 8,
              "system:index": "0"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.873822246582108, 11.233653192331456]),
            {
              "landcover": 8,
              "system:index": "1"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.873146329910355, 11.23374790184695]),
            {
              "landcover": 8,
              "system:index": "2"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.873489652664261, 11.233158597689856]),
            {
              "landcover": 8,
              "system:index": "3"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.835442993485799, 11.299274784503686]),
            {
              "landcover": 8,
              "system:index": "4"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.831505510651937, 11.30005332860509]),
            {
              "landcover": 8,
              "system:index": "5"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.830979797685018, 11.29967457768466]),
            {
              "landcover": 8,
              "system:index": "6"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.830582830750814, 11.299548327266676]),
            {
              "landcover": 8,
              "system:index": "7"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.827053043687215, 11.299621973350593]),
            {
              "landcover": 8,
              "system:index": "8"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.828576538407674, 11.29868561458946]),
            {
              "landcover": 8,
              "system:index": "9"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.827546570145955, 11.298264778195337]),
            {
              "landcover": 8,
              "system:index": "10"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.830733034455648, 11.299411555917802]),
            {
              "landcover": 8,
              "system:index": "11"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.834842178666463, 11.298706656392948]),
            {
              "landcover": 8,
              "system:index": "12"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.834981653535237, 11.299074887704185]),
            {
              "landcover": 8,
              "system:index": "13"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.835024568879476, 11.299863953207405]),
            {
              "landcover": 8,
              "system:index": "14"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.828361961686483, 11.296118502979777]),
            {
              "landcover": 8,
              "system:index": "15"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.82767531617867, 11.2957292258524]),
            {
              "landcover": 8,
              "system:index": "16"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.827621671998372, 11.297665085266713]),
            {
              "landcover": 8,
              "system:index": "17"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.82816884263741, 11.297212684508308]),
            {
              "landcover": 8,
              "system:index": "18"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.82866236909615, 11.296939139517491]),
            {
              "landcover": 8,
              "system:index": "19"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.829735252702108, 11.296770804008855]),
            {
              "landcover": 8,
              "system:index": "20"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.831838104569783, 11.296339443817056]),
            {
              "landcover": 8,
              "system:index": "21"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.833114836060872, 11.296981223379216]),
            {
              "landcover": 8,
              "system:index": "22"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.833383056962361, 11.297086433006504]),
            {
              "landcover": 8,
              "system:index": "23"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.833350870454183, 11.296570905464042]),
            {
              "landcover": 8,
              "system:index": "24"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.834477398240438, 11.297349456905875]),
            {
              "landcover": 8,
              "system:index": "25"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.834134075486531, 11.297770294643145]),
            {
              "landcover": 8,
              "system:index": "26"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.834520313584676, 11.296918097584314]),
            {
              "landcover": 8,
              "system:index": "27"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.827385637605062, 11.296339443817056]),
            {
              "landcover": 8,
              "system:index": "28"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.832063410127034, 11.298369987351762]),
            {
              "landcover": 8,
              "system:index": "29"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.832277986848226, 11.298559363736068]),
            {
              "landcover": 8,
              "system:index": "30"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.832514021241536, 11.298706656392948]),
            {
              "landcover": 8,
              "system:index": "31"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.829037878358236, 11.298369987351762]),
            {
              "landcover": 8,
              "system:index": "32"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.826505873048177, 11.298832907181492]),
            {
              "landcover": 8,
              "system:index": "33"
            }),
        ee.Feature(
            ee.Geometry.Point([-15.826291296326986, 11.299295826263943]),
            {
              "landcover": 8,
              "system:index": "34"
            })])


# Combine training samples
newfc = mangal.merge(palmar).merge(dunar)\
    .merge(agua)\
    .merge(pradohumido)\
    .merge(secundario)\
    .merge(floresta)\
    .merge(cajual)\
    .merge(povoacao)

# collect dataf from samples
training = stck.sampleRegions(newfc, ['landcover'], 30)

# fit a random forests model\
classifier = ee.Classifier.randomForest(50)\
  .train(training, 'landcover', all_bands);

# produce the forest change map
classified = stck.classify(classifier)

# accuracy assessement
confMat = classifier.confusionMatrix()
#print('Confusion matrix: ', confMat);
#print('Overall accuracy: ', confMat.accuracy());

# Create a palette to display the classes.
paleta = [
  'BD4BD5', # mangal 0
  '25A347', # palmar 1
  'F8FF25', # dunar 2
  '04C5FF', # agua 3
  '21FF32', # pradohumido 4
  'D4C452', # secundario 5
  '866418', # floresta 6
  'BE2E5D', # cajual 7
  'D6D6D6' # povoacao 8
  ]

# Add Layers
Map.centerObject(newfc, 13);

Map.addLayer(newfc, {'color': 'orange'}, 'trainingP')
Map.addLayer(classified, {"min": 0, "max": 8, "palette": paleta},'classification')
Map.addLayer(image1, trueColour, "image1")
Map.addLayer(image2, trueColour2, "image2")
