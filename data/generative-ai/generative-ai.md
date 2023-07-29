# generative-AI-101

- [Generative AI 101](#generative-ai-101)
  - [OpenAI Function calls](#openai-function-calls)
  - [Hello Worlds using Chat GPT](#Hello-world-using-chatgpt)
  - [Prompt Engineering for Developers](#Prompt-Engineering-for-developers)
  - [Tracking Prompts (PromptLayer)](#tracking-prompts-promptlayer)
  - [LangChain - What is it?](#2-langchain---what-is-it)
  - [AI Hackathon Stack (Latent Space Demo Day)](#3-ai-hackathon-stack-latent-space-demo-day)
    - [LLM/Prompt Engineering Apps](#llmprompt-engineering-apps)
      - [Templates/Example Apps/Tutorials](#templatesexample-appstutorials)
      - [Tools to explore](#tools-to-explore)
      - [Hackathon Entry Examples](#hackathon-entry-examples)
    - [Code AI tools](#code-ai-tools)
      - [Tutorials](#tutorials)
      - [Tools to explore](#tools-to-explore-1)
      - [Hackathon Entry Examples](#hackathon-entry-examples-1)
    - [Audio/Visual/Multimodal Apps](#audiovisualmultimodal-apps)
      - [Tools to explore](#tools-to-explore-2)
      - [Hackathon Entry Examples](#hackathon-entry-examples-2)
     - [AI Infra and Tooling](#ai-infra-and-tooling)
     - [AI Podcasts and Newsletters](#ai-podcasts-and-newsletters)
     - [Vector Databases](#vector-databases)

# OpenAI function calls (June) 

https://github.com/skirtapaieo/generative-AI-101/blob/main/open-ai-function-calls.ipynb by @svpino at https://github.com/svpino/openai-function-calling/blob/main/sample.ipynb

# Hello World using ChatGPT (May) 

Last slide from Andrej Karpathys presentation at 2023-05-23 on Microsoft Build 
https://github.com/skirtapaieo/generative-AI-101/blob/main/Hello-world-kind-of.ipynb 

Link to presentation --> https://t.co/HDJix905Gy




# Prompt Engineering for Developers 

I think you are looking for information on ChatGPT Prompt Engineering for Developers. This is a short course taught by Isa Fulford (OpenAI) and Andrew Ng (DeepLearning.AI) that describes how LLMs work, provides best practices for prompt engineering, and shows how LLM APIs can be used in applications for a variety of tasks, including inferring (e.g., sentiment classification, topic extraction)

https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/1/introduction

# 1 Tracking Prompts (PromptLayer) 

PromptLayer https://docs.promptlayer.com/what-is-promptlayer/wxpF9EZkUwvdkwvVE9XEvC/how-promptlayer-works/dvgGSxNe6nB1jj8mUVbG8r

# 2 LangChain - what is it? 

LangChain, created by Harrison Chase, is a Python library that provides out-of-the-box support to build NLP applications using LLMs. You can connect to various data and computation sources, and build applications that perform NLP tasks on domain-specific data sources, private repositories, and much more. 
https://github.com/skirtapaieo/generative-AI-101/blob/main/langchain.ipynb

# 3 AI Hackathon Stack (Latent Space Demo Day)

https://github.com/swyxio/ai-notes/blob/main/Resources/AI-hackathon-stack.md

## LLM/Prompt Engineering Apps

- **Templates/Example Apps/Tutorials**
  - Browse through all the [HuggingFace Spaces](https://huggingface.co/spaces)
  - [Deploying AI Applications on Vercel](https://vercel.com/blog/deploying-ai-applications) Overview and open source templates
	  - with [streaming edge functions](https://vercel.com/blog/gpt-3-app-next-js-vercel-edge-functions)
  - [LangChain + Pinecone GPT assistant tutorial](https://www.youtube.com/watch?v=15TDwVSpwKc), from PineCone
  - https://github.com/nat/natbot: Drive a browser with GPT-3. [Demo tweet video](https://twitter.com/natfriedman/status/1575631194032549888)
  - ChatGPT Plugins
	  - https://replit.com/@bardia/ChatGPT-Todo-Plugin
	  - https://replit.com/@bardia/ChatGPT-Retrieval-Plugin
	  - https://github.com/transitive-bullshit/chatgpt-plugin-ts
	  - https://supabase.com/blog/building-chatgpt-plugins-template
	  - Build a ChatGPT Plugin on Cloudflare Workers: [Tutorial](https://blog.cloudflare.com/magic-in-minutes-how-to-build-a-chatgpt-plugin-with-cloudflare-workers/); [Quickstart](https://github.com/cloudflare/chatgpt-plugin/tree/main/example-plugin)
- **Tools to explore**
  - **LLM APIs**
    - **OpenAI** needs no introduction. [Cookbook](https://github.com/openai/openai-cookbook/), [Docs](https://platform.openai.com/docs/introduction/overview)
  - **Prompt Engineering Libraries**
    - [**LangChain**](https://github.com/hwchase17/langchain/) - Building applications with LLMs through composability. [Discord](https://discord.gg/6adMQxSpJS). [ChatGPT tutorial](https://twitter.com/sjwhitmore/status/1601254826947784705).
    - [**Lambdaprompt**](https://github.com/approximatelabs/lambdaprompt) - Build, compose and call templated LLM prompts
    - [**Promptable**](https://github.com/cfortuner/promptable) - Build LLM apps in Typescript/Javascript.
  - **Embeddings**
    - [**Chroma**](https://www.trychroma.com/): Chroma is the open-source embedding database. Chroma makes it easy to build LLM apps by making knowledge, facts, and skills pluggable for LLMs. [Docs](https://docs.trychroma.com/), [Discord](https://discord.gg/MMeYNTmh3x), [@ the founders](https://twitter.com/atroyn/status/1625568377766035456?s=20&t=m96ilnMSQjoyjVmp_kQHZA)
    - [**Pinecone**](https://www.pinecone.io/): The Pinecone vector database makes it easy to build high-performance vector search applications. [Docs](https://www.pinecone.io/docs/), [Events/Forum/Showcase](https://www.pinecone.io/community/).
    
  - **Hackathon Entry Examples**
  - Automatic permit application generation for climate tech companies & carbon dioxide removal ([tweet](https://twitter.com/russelljkaplan/status/1616957750940176384?s=20&t=frXEVPqaJUjMPJOhbD9AUg))
  - a personalized learning curriculum generator ([tweet](https://twitter.com/russelljkaplan/status/1616955367728222208?s=20&t=KIszRKntkT4Y-I-WwKI8Mg))

## Code AI tools

Where the focus is building AI tools for other developers.

- **Tutorials**
  - [Build a GitHub support bot with GPT3, LangChain, and Python](https://dagster.io/blog/chatgpt-langchain) - Dagster blog ChatGPT clone ([tweet thread](https://twitter.com/floydophone/status/1612529024567500800?s=20)). Led to Astro's [HoustonAI](https://github.com/withastro/houston.astro.build): Astro AI support Bot
- **Tools to explore**
  - [OpenAI Codex](https://platform.openai.com/docs/models/codex) needs no introduction.
  - [Copilot Explorer](https://thakkarparth007.github.io/copilot-explorer/posts/copilot-internals.html#other-random-tidbits) Tools for those reverse engineering copilot. You can also peek at [GitHub Copilot Labs](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-labs).
  - https://github.com/fauxpilot/fauxpilot This is an attempt to build a locally hosted version of [GitHub Copilot](https://copilot.github.com/). It uses the [SalesForce CodeGen](https://github.com/salesforce/CodeGen) models inside of NVIDIA's [Triton Inference Server](https://developer.nvidia.com/nvidia-triton-inference-server) with the [FasterTransformer backend](https://github.com/triton-inference-server/fastertransformer_backend/).
  - The Stack: 3 TB of permissively licensed source code in 30 programming languages https://huggingface.co/datasets/bigcode/the-stack
  - _have something to add? send a PR!_
- **Hackathon Entry Examples** aiming for Open Source ones, for inspo and study
  - 🏆 [GPT is all you need for backend](https://github.com/TheAppleTucker/backend-GPT): a backend and database that is entirely LLM-powered. ([tweet](https://twitter.com/karpathy/status/1618311660539904002))
  - [KnowledgeGPT](https://github.com/mmz-001/knowledge_gpt)
  - [Chatbase.co](https://twitter.com/yasser_elsaid_/status/1621954428105379846): LangChain + Pinecone + OpenAI
  - GPT-3 Auditor: scanning code for vulnerabilities with LLMs. https://github.com/handrew/gpt3-auditor
  - [Gptcommit: Never write a commit message again (with the help of GPT-3)](https://zura.wiki/post/never-write-a-commit-message-again-with-the-help-of-gpt-3/)
  - [santacoder typosaurus]([url](https://twitter.com/corbtt/status/1616270918774575105)) - semantic linter that spots errors in code
  - stackoverflow.gg https://twitter.com/bentossell/status/1622513022781587456
  - Buildt -  AI-powered search allows you to find code by searching for what it does, not just what it is. https://twitter.com/AlistairPullen/status/1611011712345317378

## Audio/Visual/Multimodal Apps

- **Tools to explore**
  - https://www.synthesia.io/ AI video and voice creation
  - **Hosted Stable Diffusion**
    - https://replicate.com/stability-ai/stable-diffusion
    - https://replicate.com/cjwbw/stable-diffusion-v2
  - **Stable Diffusion UIs**
    - https://github.com/AUTOMATIC1111/stable-diffusion-webui
    - https://github.com/carefree0910/carefree-creator
    - https://www.charl-e.com/ 
    - https://github.com/brycedrennan/imaginAIry
  - **Transcription/Whisper**
    - https://github.com/openai/whisper
    - https://github.com/ggerganov/whisper.cpp
    - https://github.com/m-bain/whisperX
    - https://github.com/zackees/transcribe-anything 
    - https://github.com/mayeaux/generate-subtitles
  - **Multimodal, semantic video search**
    - Twelve Labs: Example: https://youtu.be/484hydNEJC0
      - Docs https://docs.twelvelabs.io/docs/understand
  - **Youtube semantic video search**
    - [Atlas](https://atlas.atila.ca/)
      - Demo: https://twitter.com/tomiwa1a/status/1617373731135029249
      - How it works: https://atila.ca/blog/tomiwa/atlas
      - Source Code: https://github.com/atilatech/atila-core-service/tree/master/atlas
  - **Computer Vision**
    - [**Roboflow**](https://roboflow.com): Build classification, object detection, and instance segmentation datasets and models. Explore over 10,000 open source models and millions of labeled images on [**Universe**](https://universe.roboflow.com). (See Roboflow Hackathon projects like visual [chess solving apps](https://devpost.com/software/chess-boss),  [automatic dog treat release](https://www.hackster.io/satoshiii/visionai-automatic-dog-treat-dispenser-wroboflow-and-yolov5-a71fd2).)
    - 10k open source models, 10M+ open source labeled images: https://universe.roboflow.com
  - _have something to add? send a PR!_
- **Hackathon Entry Examples**
  - HouseGPT generates raw MIDI data directly from few-shot prompted GPT-3 to create 🎶 house music 🎶 🔊 ([tweet](https://twitter.com/russelljkaplan/status/1616997544307089408?s=20&t=frXEVPqaJUjMPJOhbD9AUg))
  - [Rap Battle](https://twitter.com/russelljkaplan/status/1617070021406265345?s=20&t=frXEVPqaJUjMPJOhbD9AUg) - Pick any two people and it will generate a rap battle on the fly, using GPT-3 for lyrics, wavenet for vocals, and stable diffusion for the avatars. 
  - Game of Life, where each alive cell is a whimsical happy Stable Diffusion image and each dead cell is an eerie, dark Stable Diffusion image, all of which evolve over time. ([tweet](https://twitter.com/russelljkaplan/status/1616955356189687810?s=20&t=KIszRKntkT4Y-I-WwKI8Mg))

## AI Infra and Tooling

This category is for **infra and tools** catering to AI app developers, in contrast to **apps** (below) which have other kinds of end users in mind.

- **Tools to explore**
  - **Serverless GPUs**
    - https://exafunction.com/ Exafunction optimizes your deep learning inference workload, delivering up to a 10x improvement in resource utilization and cost.
    - https://www.banana.dev/ Scale your machine learning inference and training on serverless GPUs.
    - https://brev.dev/ The simplest way to create a dev environment with a GPU. Don't worry about dependencies, CUDA, SSH, or anything else. Up to 94% cheaper GPUs than AWS. For example: here's a guide to get a GPU dev environment to train your own Dreambooth model in ~4 min 🤙 https://brev.dev/docs/guides/dreambooth
    - https://lambdalabs.com/ GPU cloud built for deep learning. Instant access to the best prices for cloud GPUs on the market. No commitments or negotiations required. Save over 73% vs AWS, Azure, and GCP. Configured for deep learning with PyTorch®, TensorFlow, Jupyter
    - https://www.paperspace.com/ Paperspace provides tooling for training and serving, with serverless GPUs, development environments, and workflow management systems.
    - More serverless discussions: https://news.ycombinator.com/item?id=34742087
    - _Seeking: hackathon-relevant examples and tutorials for each of these tools_
  - **Model Serving**
    - https://www.baseten.co/ Serverless backend for building ML-powered applications. Build apps with auto-scaling, GPU access, CRON jobs, and serverless functions.
    - https://replicate.com/ Run models in the cloud at scale.
    - https://modal.com run or deploy machine learning models, massively parallel compute jobs, task queues, web apps, and much more, without your own infrastructure.. Example [serving Stable Diffusion API](https://modal.com/docs/guide/ex/stable_diffusion_slackbot), [BERT in 34 lines of code](https://news.ycombinator.com/item?id=35792481)
    - https://www.steamship.com/ Managed Backend for AI services [LangChain example](https://www.steamship.com/build/langchain-apps)
    - [https://www.coreweave.com/](https://www.coreweave.com/)
    - vast.ai
    - [Cloudflare Constellation](https://blog.cloudflare.com/introducing-constellation/) - deploy models and run inferencing on Cloudflare's edge
    - _Seeking: hackathon-relevant examples and tutorials for each of these tools_
    - _Seeking: tutorials for serving Whisper, other LLMs_
  - **Fine-tuning**
    - [Blueprint by Baseten](https://app.baseten.co/blueprint/signup/) Fine-tuning and serving of foundation models. [Docs](https://docs.blueprint.baseten.co/). In alpha; reach out on Discord to Amir H. for help. 
  - **Evaluation**
    - [Zeno](https://zenoml.com) Interactive data management and evaluation for foundational models. [Docs](https://zenoml.com/docs/intro) and [Demos](https://zenoml.com/docs/demos).
  - _have something to add? send a PR!_
- **Hackathon Entry Examples**
  -  a key-value store to enable long-term memory in language model conversations ([tweet](https://twitter.com/russelljkaplan/status/1616955361705197568?s=20&t=KIszRKntkT4Y-I-WwKI8Mg))

# AI podcasts and newsletters 

## Podcasts

some of these are on youtube too, i dont really bother separating them

- Researchers & Specialists
	- [The Gradient](https://thegradientpub.substack.com/s/podcast) (Daniel Bashir) - gerat practitioner interviews
	- [Practical AI](https://changelog.com/practicalai) (Dan Whitenack) - good weekly conversations, a bit enterprisey
	- [This Week in Machine Learning/AI](https://twimlai.com/podcast/twimlai/) (Sam Charrington) - one of the longest running practitioner interview shows
	- [Machine Learning Street Talk](https://www.youtube.com/c/MachineLearningStreetTalk) (Tim Scarfe) - great backlog of safety/philosophy researcher interviews
	- [The Inside View](https://theinsideview.ai/) (Michael Trazzi) - safety researcher interviews. infrequent.
- News/Youtubers
	- [Last Week in AI](https://lastweekin.ai/)- quite long news recap but very consistent and well organized
	- [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) - paper reviews and news recaps
	- [AI Explained](https://www.youtube.com/@ai-explained-) - news recaps
	- [The ChatGPT report](https://anchor.fm/ben-meyerhoeffer/episodes/Ep-30-Bard-vs-Bing-e212edr) - 10 minutes on AI news Mondays and Thursdays
	- [Eye on AI](https://open.spotify.com/show/5aFnCGDhpL5bGr2uHy4bB5) - Weekly analysis at the intersection of artificial intelligence and industry. (Great guest backlog)
- Companies
	- [Deep Papers](https://www.deeppapers.dev/) - Arize AI/AI Pub - focusing on paper reviews
	- [Gradient Dissent](https://www.youtube.com/playlist?list=PLD80i8An1OEEb1jP0sjEyiLG8ULRXFob_) - Weights and Biases - Lukas is a great host
	- [Robot Brains](https://www.therobotbrains.ai/) - Pieter Abbeel - ddecent backlog
	- [The Cognitive Revolution](https://www.cognitiverevolution.ai/) - Nathan Labenz - kinda new, some good chats
	- [Generally Intelligent](https://generallyintelligent.com/podcast) - Kanjun Qiu - very cerebral/RL focused
	- [NLP Highlights](https://www.listennotes.com/podcasts/nlp-highlights-allen-institute-for-f9Yt4vD_ger/) by the Allen Institute (infrequent but good pre 2020 backlog. Check episode 36j)
- VCs
	- [No Priors](https://linktr.ee/nopriors) - Sarah Guo and Elad Gil - new
	- [Unsupervised Learning](https://podtail.com/en/podcast/unsupervised-learning/) - Redpoint - new
- Mine :) https://latent.space/ - new

## Newsletters

- Leaders
	- Andrew Ng's [The Batch](https://www.deeplearning.ai/the-batch/)  picks 3 things each week and summarizes approachably
	- Jack Clark's [Import AI](https://importai.substack.com/) focused more on policy given Jack's role
	- Sebastian Raschka [Ahead of AI](https://magazine.sebastianraschka.com/) deeply technical recaps
- Commentators/ML Eng's
	- Alan Thompson's Life Architect https://lifearchitect.substack.com (note [his credentials sus](https://news.ycombinator.com/item?id=35588974))
	- Bradley Metrock (Deepgram) https://thisweekinvoice.substack.com/
	- Carlos's Data Machina https://datamachina.substack.com/
	- Davis Blalock Arxiv roundup https://dblalock.substack.com/
- Aggregators
	- Socially ranked papers weekly https://papers.labml.ai/papers/weekly (has [chrome extension](https://github.com/labmlai/chrome-extension)) - see also Karpathy's [arxiv-sanity](https://arxiv-sanity-lite.com/)
	- TheSequence https://thesequence.substack.com/about (paid & free)
	- Ben's Bites https://bensbites.beehiiv.com/
	- Rachel Woods' The AI Exchange https://theaiexchange.beehiiv.com/
	- Pete Huang's The Neuron https://www.theneurondaily.com/
	- Lior AlphaSignal https://alphasignal.ai/
	- Bot Eat Brain https://www.boteatbrain.com/
- Mine :) https://latent.space/

# 3 Vector databases 

- [Pinecone](https://www.pinecone.io/)
- [Faiss](https://github.com/facebookresearch/faiss)
- [Annoy](https://github.com/spotify/annoy)
- [Milvus](https://milvus.io/)
- [SPTAG](https://github.com/microsoft/SPTAG)
- [HNSW (Hierarchical Navigable Small World)](https://github.com/nmslib/hnswlib)
- [NGT (Neighborhood Graph and Tree for Indexing High-dimensional Data)](https://github.com/yahoojapan/NGT)
- [Weaviate](https://www.semi.technology/developers/weaviate/current/)
- [Vespa](https://vespa.ai/)


