---
title: Speech recognition services
type: reference
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: fal.ai/elevenlabs, help.elevenlabs.io (restricted countries), deepgram.com (pricing, Nova-3 languages changelog 2026-08-17), soniox.com (pricing, benchmarks), assemblyai.com (pricing, models, benchmarks), artificialanalysis.ai (speech-to-text leaderboard), mistral speech pricing reviews (developersdigest.tech, digitalapplied.com), console.groq.com/docs/models, cloud.google.com/speech/pricing, convertaudiototext.com (API prices), aistudio.yandex.ru, alphacephei.com/vosk/android [Claude] 2026-11-13
parent: 20-device.md
---

# Speech recognition services

Comparison for the [voice order notebook](functions.md#2-voice-order-notebook). Voice runs in the cloud through the server's phone `[A]` 2026-11-13, see the [decision log](../70-decisions/70-decisions.md#2026-11-13-voice-runs-in-the-cloud-through-the-phone). The device is not used in Russia, and payment from abroad is possible `[A]` 2026-11-13. Thus the limits of services for Russia do not apply.

Limit: web research only `[Claude]` 2026-11-13. No service was tested on real speech. Prices come from vendor pages and reviews; some reviews do not agree. No independent Russian benchmark for all services was found. Check the vendor page before you pay.

## What the device needs

1. Russian speech, short phrases of 3 to 6 s: "table seven, seat two, carbonara without bacon".
2. Noise of the restaurant floor.
3. Menu words: dish names, often borrowed words. Keyterms (a list of words that the service must expect) help.
4. Streaming or a fast short request: the server waits for the result.

## Comparison

Prices in USD. "Realtime" means streaming.

| Service | Model | Price | Keyterms | Russian | Notes |
|---|---|---|---|---|---|
| ElevenLabs | Scribe v2 | 0.22/h batch, 0.39/h realtime | yes, up to 1,000 | yes | best results in several multilingual benchmarks |
| fal.ai | Scribe v2, Whisper and others | Scribe v2 0.008/min | as the model | as the model | 1 account and prepaid credit for several models; good for a test |
| Soniox | stt-rt-v6, realtime | 0.12/h | not checked `[?]` | yes | the vendor says it is more accurate in Russian than Deepgram; not independent |
| Deepgram | Nova-3, realtime | about 0.46/h (0.0077/min); keyterms +0.0013/min | yes | yes, monolingual model `ru`; improved 2026-08 | sub-300 ms streaming |
| AssemblyAI | Universal-3.6 Pro Realtime | 0.45/h | yes, included, up to 100 | yes | the cheaper multilingual streaming model has no Russian |
| OpenAI | gpt-4o-transcribe, mini | 0.006 and 0.003/min | text prompt | yes | weak on mixed-language speech in 1 benchmark |
| Mistral | Voxtral Mini Transcribe 3 | 0.21/h batch; realtime 0.006 to 0.008/min | custom vocabulary, 1 source `[?]` | not confirmed `[?]` | |
| Groq | Whisper large-v3-turbo | 0.04/h, minimum 10 s per request | no | yes | files only, no streaming; very fast |
| Google | Chirp | 0.016/min | phrase hints | yes | not checked further |

Other options from the first version of this page. Yandex SpeechKit: about 0.16 RUB for 15 s, billed in 15 s steps. Vosk runs offline on an Android phone, free, with a word list; it is usually less accurate `[?]`.

## Cost per shift

Estimate `[?]`: 60 voice entries per shift, 5 s each, 5 min of speech in total.

With any service in the table, a shift costs less than 0.05 USD. The price does not decide the choice. Accuracy on the floor and the keyterms decide it.

## Findings

1. ElevenLabs Scribe v2 is the first candidate: the best benchmark results, streaming and up to 1,000 keyterms. The full menu fits in the keyterms.
2. Soniox and Deepgram Nova-3 are the next candidates: streaming, keyterms (Deepgram), low price.
3. fal.ai is useful for the test: 1 account gives Scribe v2 and Whisper.
4. Groq is the cheapest and fast, but it has no streaming and no keyterms.

## Proposed test

Status: proposed `[Claude]` 2026-11-13. Artemy decides.

1. Record 30 order phrases on the floor with the phone, or in a noisy room. Use real menu items. Keep the recordings in `_private/`.
2. Write the correct text for each phrase.
3. Send the same recordings to ElevenLabs Scribe v2, Soniox, Deepgram Nova-3 and OpenAI gpt-4o-transcribe. Give the menu items as keyterms where the service supports them.
4. Count the phrases where the table, the seat and the dish are all correct. Measure the time to the result.
5. Choose the service with the best count. Write the result and the decision in the [decision log](../70-decisions/70-decisions.md).

[Parent](20-device.md)
