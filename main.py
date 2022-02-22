from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return [
	    {
		"artist": "Ink Waruntorn",
	    "song":"กลับก่อนนะ",
	    "duration" : "160",
	    "brand" : "Boxx music",
	    "image" : "https://soranatch4.com/demo-ink/assets/img/ink-0001.jpeg"
	    },
	     {
		"artist": "Ink Waruntorn",
	    "song":"ลบไม่ได้ช่วยให้ลืม",
	    "duration" : "220",
	    "brand" : "Boxx music",
	    "image" : "https://soranatch4.com/demo-ink/assets/img/ink-0002.jpeg"
	    },
	     {
		"artist": "Ink Waruntorn",
	    "song":"อยากเริ่มต้นใหม่กับคนเดิม",
	    "duration" : "210",
	    "brand" : "Boxx music",
	    "image" : "https://soranatch4.com/demo-ink/assets/img/ink-0003.jpeg"
	    },
	     {
		"artist": "Ink Waruntorn",
	    "song":"เหนื่อยใจ",
	    "duration" : "180",
	    "brand" : "Boxx music",
	    "image" : "https://soranatch4.com/demo-ink/assets/img/ink-0004.jpeg"
	    },    
	    ]
