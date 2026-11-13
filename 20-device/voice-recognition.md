---
title: Speech recognition services
type: reference
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: fal.ai/elevenlabs, help.elevenlabs.io (restricted countries), elevenlabs.io/terms-of-use, deepgram.com (pricing, Nova-3 languages changelog 2026-08-17), soniox.com (pricing, benchmarks), assemblyai.com (pricing, models), mistral speech pricing reviews (developersdigest.tech, digitalapplied.com), console.groq.com/docs/models, cloud.google.com/speech/pricing, help.openai.com (supported countries), fal.ai/legal/acceptable-use-policy, aistudio.yandex.ru, developers.sber.ru, alphacephei.com/vosk/android [Claude] 2026-11-13
parent: 20-device.md
---

# Speech recognition services

Comparison for the [voice order notebook](functions.md#2-voice-order-notebook). Voice runs in the cloud through the server's phone `[A]` 2026-11-13, see the [decision log](../70-decisions/70-decisions.md#2026-11-13-voice-runs-in-the-cloud-through-the-phone). Payment from outside Russia is possible `[A]` 2026-11-13. Thus this page compares mainly services outside Russia.

Limit: web research only `[Claude]` 2026-11-13. No service was tested on real speech. Prices come from vendor pages and reviews; some reviews do not agree. No independent Russian benchmark for all services was found. Check the vendor page before you pay.

## What the device needs

1. Russian speech, short phrases of 3 to 6 s: "table seven, seat two, carbonara without bacon".
2. Noise of the restaurant floor.
3. Menu words: dish names, often borrowed words. Keyterms (a list of words that the service must expect) help.
4. Streaming or a fast short request: the server waits for the result.
5. The service accepts requests from a phone in Russia.

## Use from Russia

Payment from abroad does not remove all limits. The phone sends the requests from Russia. Some services forbid use from Russia in their terms, not only payment from Russia.

| Service | Use from Russia |
|---|---|
| ElevenLabs | forbidden: Russia is on its list of restricted countries |
| OpenAI | forbidden: Russia is not a supported country |
| fal.ai | its terms forbid "Restricted Territories" under sanctions; the list was not read `[?]` |
| Deepgram, Soniox, AssemblyAI, Mistral, Groq, Google | not checked `[?]`. Read the terms before you make an account |

Do not use a service whose terms forbid use from Russia. The account can be closed without notice.

## Comparison

Prices in USD. "Realtime" means streaming.

| Service | Model | Price | Keyterms | Russian | Notes |
|---|---|---|---|---|---|
| Soniox | stt-rt-v6, realtime | 0.12/h | not checked `[?]` | yes | the vendor says it is more accurate in Russian than Deepgram; not independent |
| Deepgram | Nova-3, realtime | about 0.46/h (0.0077/min); keyterms +0.0013/min | yes | yes, monolingual model `ru`; improved 2026-08 | sub-300 ms streaming |
| AssemblyAI | Universal-3.6 Pro Realtime | 0.45/h | yes, included, up to 100 | yes | the cheaper multilingual streaming model has no Russian |
| Mistral | Voxtral Mini Transcribe 3 | 0.21/h batch; realtime 0.006 to 0.008/min | custom vocabulary, 1 source `[?]` | not confirmed `[?]` | company in the EU |
| Groq | Whisper large-v3-turbo | 0.04/h, minimum 10 s per request | no | yes | files only, no streaming; very fast |
| ElevenLabs | Scribe v2 | 0.22/h batch, 0.39/h realtime; through fal.ai 0.008/min | yes, up to 1,000 | yes | best results in several multilingual benchmarks; use from Russia forbidden |
| OpenAI | gpt-4o-transcribe, mini | 0.006 and 0.003/min | text prompt | yes | use from Russia forbidden |
| Google | Chirp | 0.016/min | phrase hints | yes | not checked further |

Services in Russia, from the first version of this page, have no access risk. Yandex SpeechKit: about 0.16 RUB for 15 s, billed in 15 s steps. SaluteSpeech: a package of 1,000 min for 1,200 RUB a month for a private person, with word hints, up to 100. Vosk runs offline on an Android phone, free, with a word list; it is usually less accurate `[?]`.

## Cost per shift

Estimate `[?]`: 60 voice entries per shift, 5 s each, 5 min of speech in total.

With all services outside Russia, a shift costs less than 0.05 USD. The price does not decide the choice. Accuracy on the floor, the keyterms and the use from Russia decide it.

## Findings

1. ElevenLabs Scribe v2 has the best benchmark results, but its terms forbid use from Russia. fal.ai resells it and also has a sanctions clause.
2. OpenAI is out for the same reason.
3. Soniox, Deepgram Nova-3 and AssemblyAI Universal-3.6 Pro are the best candidates outside Russia: Russian, streaming, keyterms. Their terms for Russia are not checked yet.
4. Groq is the cheapest and fast, but it has no streaming and no keyterms.
5. Yandex SpeechKit stays as the fallback in Russia.

## Proposed test

Status: proposed `[Claude]` 2026-11-13. Artemy decides.

1. Read the terms of Soniox, Deepgram and AssemblyAI for use from Russia. Keep only the services that allow it.
2. Record 30 order phrases on the floor with the phone, or in a noisy room. Use real menu items. Keep the recordings in `_private/`.
3. Write the correct text for each phrase.
4. Send the same recordings to the remaining services and to Yandex SpeechKit. Give the menu items as keyterms where the service supports them.
5. Count the phrases where the table, the seat and the dish are all correct. Measure the time to the result.
6. Choose the service with the best count. Write the result and the decision in the [decision log](../70-decisions/70-decisions.md).

[Parent](20-device.md)
