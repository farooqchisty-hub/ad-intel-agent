# Batch 2 options (13 Nov 2026, after Farooq's review): 3 real examples per ad that shows winners or clones.
# Befores: real Ad Radar winners shown exactly as they ran (no blur), run length from Ad Radar on 13 Nov 2026.
# Afters: real Clone runs in Ad Studio (GPT Image 2.5, 2 variants per run, the closer variant shown)
# for the redesigned demo brands glowday (tinted mineral SPF 50) and drift (magnesium sleep gummies).

RADAR = "https://ads.brevo.com/ad-radar/creative/"
CDN = "https://media.powlcdn.com/magicfit/"

WIN = {
    "norse": dict(brand="Norse Organics", text="NO ONE'S LOVE LANGUAGE IS ACNE.", days=479, uuid="e5895f64-b67e-4f6a-a20c-8cbfbc2fa97a", meta="601927446093327", img="w7_479d.jpg"),
    "seed": dict(brand="Seed", text="Is your probiotic actually effective?", days=271, uuid="53174361-0c7d-4000-a12f-58be7eabb25f", meta="1287242396751521", img="w101_271d.jpg"),
    "ghost": dict(brand="GHOST", text="BUILD A STACK THAT SLAPS", days=198, uuid="465d199a-23b2-48f2-a96d-95d9577d2d08", meta="1516073733167797", img="w195_198d.jpg"),
    "huel_glp1": dict(brand="Huel", text="GLP-1 killed your appetite. Not your nutritional needs.", days=187, uuid="0d5f685a-ea6b-402b-b692-a33f0de1e031", meta="920503093803810", img="w231_187d.jpg"),
    "lovevery": dict(brand="Lovevery", text="My coffee's hot / My baby's happy", days=161, uuid="84655cf1-bb18-4c89-954b-9728529ce775", meta="1683133726354180", img="w389_161d.jpg"),
    "headspace": dict(brand="Headspace", text="Sleep like a dog", days=163, uuid="7f5ee947-90d0-45f2-a33d-cee020d78fc1", meta="2158139111630035", img="w364_163d.jpg"),
    "gainful": dict(brand="Gainful", text="Does protein make you bloated?", days=182, uuid="9d4df54a-3b5b-4dbf-87f3-380ae1cfa06f", meta="1303389214560608", img="w252_182d.jpg"),
    "merit": dict(brand="Merit", text="SPF you'll forget you're wearing", days=182, uuid="60660e1a-a143-41e1-b6a8-d255abc04eaa", meta="1204026872785047", img="w250_182d.jpg"),
    "kc_clock": dict(brand="Ka'Chava", text="like clockwork", days=165, uuid="b256eb49-7a49-405c-adb6-8e077f484301", meta="1455621379837838", img="w349_165d.jpg"),
    "ryze": dict(brand="RYZE", text="BLACK FRIDAY, starts now, up to 40% off", days=372, uuid="bccbc46b-06a6-41fa-8352-bd1e9da3b691", meta="1396188171889302", img="w_ryze_372d.jpg"),
    "jax_dark": dict(brand="Jaxxon", text="Up to 55% off, Black Friday sale", days=382, uuid="7505c6f5-b53c-49ce-8076-9f2b026618c2", meta="1386449166435179", img="w28_382d.jpg"),
    "jax_sky": dict(brand="Jaxxon", text="Black Friday Sale, up to 55% off", days=382, uuid="0f03eaef-9861-499e-802e-6706c6e2eade", meta="828615690104469", img="w29_382d.jpg"),
    "bark": dict(brand="BARK", text="I've got a big purple eggplant / and i'm not afraid to admit it", days=179, uuid="762a3cc1-1830-4beb-b158-66b306f2d093", meta="1341755421136657", img="w265_179d.jpg"),
    "pupford": dict(brand="Pupford", text="Having a puppy is all sh*ts and giggles", days=164, uuid="0ff0a409-d244-4d78-8efd-10da68d7ff9a", meta="1901794503848616", img="w354_164d.jpg"),
    "pandora": dict(brand="Pandora", text="don't lie, you still listen to...", days=177, uuid="ddfa03c8-a972-456f-9823-dbb1f2431d84", meta="2087329828510156", img="w282_177d.jpg"),
    "kc_again": dict(brand="Ka'Chava", text="Crackers. Nuggets. / Not again.", days=156, uuid="930346f9-7caf-4ef4-bdff-4082c8cee559", meta="1061921176165511", img="w422_156d.jpg"),
    "huel_meal": dict(brand="Huel", text="This is a meal. Not a protein shake.", days=156, uuid="edb1678d-42d1-48b0-8808-9be462f06353", meta="1227288965941007", img="w421_156d.jpg"),
    "olipop": dict(brand="Olipop", text="illustrated cream soda can", days=164, uuid="f8b3a512-ff2a-469d-a48b-d4af90cff683", meta="826800313553161", img="w356_164d.jpg"),
}

CLO = {
    "21a": dict(prod="glowday", text="NO ONE'S LOVE LANGUAGE IS WHITE CAST.", file="1794562620358-ad-1794562619687.png"),
    "21b": dict(prod="drift", text="Is your sleep aid actually working?", file="1794562993637-ad-1794562992195.png"),
    "21c": dict(prod="drift", text="BUILD A BEDTIME THAT SLAPS", file="1794566392955-ad-1794566391542.png"),
    "24a": dict(prod="drift", text="Your phone killed your sleep. Not your need for it.", file="1794565641662-ad-1794565641158.png"),
    "24b": dict(prod="glowday", text="My SPF's on / My glow's still on", file="1794563250370-ad-1794563250177.png"),
    "24c": dict(prod="drift", text="Sleep like a dog. Wake up without the fog with drift.", file="1794565637029-ad-1794565636502.png"),
    "31a": dict(prod="drift", text="Does your sleep aid leave you groggy?", file="1794565686128-ad-1794565684977.png"),
    "31b": dict(prod="glowday", text="Zinc you'll forget you're wearing.", file="1794565710578-ad-1794565709913.png"),
    "31c": dict(prod="drift", text="out like a light", file="1794565707986-ad-1794565707053.png"),
    "32a": dict(prod="glowday", text="BLACK FRIDAY, starts now, up to 25% off", file="1794565743805-ad-1794565742877.png"),
    "32b": dict(prod="glowday", text="Up to 25% off, Black Friday sale", file="1794565839837-ad-1794565838980.png"),
    "32c": dict(prod="drift", text="Black Friday Sale, up to 25% off", file="1794565770501-ad-1794565769826.png"),
    "33a": dict(prod="drift", text="I take gummies to bed every night / and i'm not afraid to admit it.", file="1794565860207-ad-1794565859139.png"),
    "33b": dict(prod="glowday", text="Your 20s are all sun and giggles. Your 40s get the bill.", file="1794565941149-ad-1794565939289.png"),
    "33c": dict(prod="glowday", text="don't lie, you still skip SPF...", file="1794565862840-ad-1794565860641.png"),
    "39a": dict(prod="drift", text="3:07 AM. Ceiling. / Not again.", file="1794565869046-ad-1794565868619.png"),
    "39b": dict(prod="glowday", text="This is SPF 50. Not foundation.", file="1794565976247-ad-1794565974454.png"),
    "39c": dict(prod="drift", text="illustrated night scene with the drift jar", file="1794566403896-ad-1794566402666.png"),
}

HL = {
    21: "{d} days of testing. Cloned in under 2 minutes.",
    23: "Stop screenshotting your competitors' ads.",
    24: "Their winner. Your product. Zero dollars.",
    31: "They paid for {d} days. You pay $0.",
    32: "Their Black Friday ad has run {d} days.",
    33: "Bet your ad can't beat {d} days.",
    35: "Free: 3 ads that already won.",
    36: "Don't clone this ad.",
    39: "Copy what works. Literally.",
}

# ad -> options: (key, [winners], clone key or None)
OPTS = {
    21: [("21a", ["norse"], "21a"), ("21b", ["seed"], "21b"), ("21c", ["ghost"], "21c")],
    23: [("23a", ["norse"], None), ("23b", ["bark"], None), ("23c", ["pandora"], None)],
    24: [("24a", ["huel_glp1"], "24a"), ("24b", ["lovevery"], "24b"), ("24c", ["headspace"], "24c")],
    31: [("31a", ["gainful"], "31a"), ("31b", ["merit"], "31b"), ("31c", ["kc_clock"], "31c")],
    32: [("32a", ["ryze"], "32a"), ("32b", ["jax_dark"], "32b"), ("32c", ["jax_sky"], "32c")],
    33: [("33a", ["bark"], "33a"), ("33b", ["pupford"], "33b"), ("33c", ["pandora"], "33c")],
    35: [("35a", ["ghost", "huel_glp1", "bark"], None), ("35b", ["ryze", "pandora", "olipop"], None), ("35c", ["seed", "headspace", "lovevery"], None)],
    36: [("36a", ["norse"], None), ("36b", ["huel_glp1"], None), ("36c", ["bark"], None)],
    39: [("39a", ["kc_again"], "39a"), ("39b", ["huel_meal"], "39b"), ("39c", ["olipop"], "39c")],
}
