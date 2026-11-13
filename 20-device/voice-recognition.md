---
title: Speech recognition services
type: reference
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: openrouter.ai (audio APIs announcement, speech-to-text collection, model pages, STT docs), fal.ai/elevenlabs, deepinfra.com/models/automatic-speech-recognition, edenai.co, artificialanalysis.ai (speech-to-text leaderboard), assemblyai.com/benchmarks, deepgram.com (Nova-3 changelog 2026-08-17), soniox.com (pricing), help.elevenlabs.io (restricted countries) [Claude] 2026-11-13
parent: 20-device.md
---

# Speech recognition services

Comparison for the [voice order notebook](functions.md#2-voice-order-notebook). Voice runs in the cloud through the server's phone `[A]` 2026-11-13, see the [decision log](../70-decisions/70-decisions.md#2026-11-13-voice-runs-in-the-cloud-through-the-phone). The device is not used in Russia, and payment from abroad is possible `[A]` 2026-11-13.

Limit: web research only `[Claude]` 2026-11-13. No service was tested on real speech. Prices come from vendor pages and reviews; some reviews do not agree. Check the platform page before you pay.

## What the device needs

1. Russian speech, short phrases of 3 to 6 s: "table seven, seat two, carbonara without bacon".
2. Noise of the restaurant floor.
3. Menu words: dish names, often borrowed words. Keyterms (a list of words that the service must expect) help.
4. A fast result. Streaming is not necessary: the server holds `TALK`, the phone sends the short recording after the release.
5. Many models from different vendors through 1 account, with prepaid credit and no subscription `[A]` 2026-11-13. The model changes with 1 parameter, so tests and later changes are easy.

## Platforms with many vendors

| Platform | Speech models (vendor) | Billing | Notes |
|---|---|---|---|
| OpenRouter | Scribe v2 (ElevenLabs), GPT Transcribe, gpt-4o-transcribe and mini (OpenAI), Voxtral Small Transcribe 3 (Mistral), Gemini 3.5 Transcribe (Google), Universal-3.5 Pro (AssemblyAI), Transcribe 1 (Fish Audio), Whisper | prepaid credit; per second or per token | 1 endpoint `/api/v1/audio/transcriptions`; the model is a parameter. Speech models since 2026 |
| fal.ai | Scribe v2 (ElevenLabs), Whisper large-v3 and Wizper, Canary streaming, Cohere Transcribe | prepaid credit; each model has its own price | also has streaming models |
| DeepInfra | Voxtral Mini and Small (Mistral), Whisper | per minute | the lowest prices; open models only |
| Eden AI | Deepgram, AssemblyAI, Speechmatics, Google and others | per minute, higher than direct | 1 API for the classic speech vendors |

Hugging Face Inference Providers also route to some of these platforms. Not checked further.

## Models to compare

Prices in USD per hour of audio, through the platform.

| Model | Platform | Price | Keyterms | Notes |
|---|---|---|---|---|
| ElevenLabs Scribe v2 | OpenRouter, fal.ai | 0.22 (OpenRouter), 0.48 (fal.ai) | through the platform: not checked `[?]` | best results in several multilingual benchmarks |
| OpenAI GPT Transcribe | OpenRouter | 0.27 | yes: keyword hints | newer than gpt-4o-transcribe |
| Mistral Voxtral Small Transcribe 3 | OpenRouter | 0.24 | not checked `[?]` | Voxtral Mini on DeepInfra: about 0.06 |
| Google Gemini 3.5 Transcribe | OpenRouter | per token, not converted `[?]` | prompt | |
| AssemblyAI Universal-3.5 Pro | OpenRouter | not checked `[?]` | not checked `[?]` | Russian is supported in Universal-3.6 Pro direct |
| Deepgram Nova-3 | OpenRouter `[?]`, Eden AI | about 0.26 | direct: yes | Russian monolingual model, improved 2026-08 |
| Whisper large-v3 | all platforms | 0.01 to 0.07 | prompt only | the reference for the comparison |

Soniox (0.12/h realtime) is on none of these platforms. It needs its own account.

## Cost per shift

Estimate `[?]`: 60 voice entries per shift, 5 s each, 5 min of speech in total. With any model in the table, a shift costs less than 0.05 USD. The price does not decide the choice. Accuracy on the floor and the keyterms decide it.

## Findings

1. OpenRouter is the first choice: 1 account and 1 endpoint give ElevenLabs, OpenAI, Mistral, Google and AssemblyAI. The model changes with 1 parameter.
2. fal.ai is the second: it adds Whisper variants and streaming models.
3. Keyterms through the platforms are not clear. Only GPT Transcribe documents keyword hints on OpenRouter. Check in the test if the platforms pass the keyterms of the other models.
4. Streaming is not necessary for push-to-talk. A short file request is enough if the time to the result is short.

## Proposed test

Status: proposed `[Claude]` 2026-11-13. Artemy decides.

1. Make an account on OpenRouter and put prepaid credit on it. Optional: fal.ai too. Put the keys in `keys/`.
2. Record 30 order phrases on the floor with the phone, or in a noisy room. Use real menu items. Keep the recordings in `_private/voice-test/`.
3. Write the correct text for each phrase.
4. Send the same recordings to Scribe v2, GPT Transcribe, Voxtral Small Transcribe 3, Gemini 3.5 Transcribe and Whisper large-v3. Give the menu items as keyterms or as a prompt where the model takes them.
5. Count the phrases where the table, the seat and the dish are all correct. Measure the time to the result.
6. Choose the model with the best count. Write the result and the decision in the [decision log](../70-decisions/70-decisions.md).

[Parent](20-device.md)
