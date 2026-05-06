# Research Repository

### 1\. Confidence-Based Self-Training for EMG-to-Speech: Leveraging Synthetic EMG for Robust Modeling

This paper introduces a novel Confidence-based Multi-Speaker Self-training (CoM2S) approach to address the scarcity of paired EMG-speech data by leveraging synthetic EMG generated from audio corpora like LibriSpeech. The researchers curate the Libri-EMG dataset, containing 8.3 hours of high-quality multi-speaker data, and demonstrate that a 1:1 mix of real and synthetic data outperforms existing baselines, reducing Word Error Rates significantly. DOI:[10.48550/arXiv.2506.11862](https://doi.org/10.48550/arXiv.2506.11862)

### 2\. Can LLMs Understand Unvoiced Speech? Exploring EMG-to-Text Conversion with LLMs

This study explores the feasibility of using frozen Large Language Models (LLMs) to decode unvoiced electromyography signals without requiring corresponding audio or voiced data. The authors propose a trainable EMG adaptor module that maps EMG features into the LLM’s input space, achieving a Word Error Rate (WER) of 0.49 with as little as six minutes of user training data. URL: [https://aclanthology.org/2025.acl-short.56](https://aclanthology.org/2025.acl-short.56)

### 3\. A Cross-Modal Approach to Silent Speech with LLM-Enhanced Recognition

This milestone research introduces the MONA LISA framework, which reduces the Word Error Rate for open-vocabulary silent speech from 28.8% to a record-breaking 12.2%. MONA (Multimodal Orofacial Neural Audio) uses cross-modal contrastive loss to align EMG with high-fidelity audio embeddings, while LISA (LLM-Integrated Scoring Adjustment) uses models like GPT-4 to correct "neuromuscular typos" in the final transcript. URL:[https://arxiv.org/abs/2403.05583](https://arxiv.org/abs/2403.05583)

### 4\. A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband

This work presents a wearable textile neckband featuring 14 fully-differential channels designed for comfortable, non-intrusive EMG acquisition. Powered by the BioGAP-Ultra platform, the system achieves 87% accuracy for vocalized speech and 68% for silent commands while consuming only 22.2 mW for biosignal acquisition and wireless transmission.URL: [https://arxiv.org/abs/2509.21964](https://arxiv.org/abs/2509.21964)

### 5\. Advances in EMG-to-Speech Generation

This resource provides a thematic overview of the transition from lab-grade arrays to discreet wearables like headphone earmuffs and neckbands. It details state-of-the-art mapping paradigms, including direct regression to acoustic features and the use of diffusion models to improve the naturalness and intelligibility of synthesized speech. URL:[https://www.emergentmind.com/topics/emg-to-speech-generation](https://www.emergentmind.com/topics/emg-to-speech-generation)

### 6\. Confidence-Based Self-Training for EMG-to-Speech: Leveraging Synthetic EMG for Robust Modeling (ArXiv Version)

This source provides the technical preprint details for the CoM2S framework, emphasizing the phoneme-level confidence filtering mechanism used to validate synthetic EMG-speech pairs. The study validates that increasing dataset scale from 3.2 hours to 16 hours leads to consistent improvements in phoneme accuracy and robustness. DOI:[10.48550/arXiv.2506.11862](https://doi.org/10.48550/arXiv.2506.11862)

### 7\. EMG-to-Speech with Fewer Channels

This research investigates channel efficiency in EMG-to-speech systems, determining that the highest performance comes from subsets that leverage complementary relationships between muscles. It demonstrates that fine-tuning a model pretrained on 8-channel data with random channel dropout consistently outperforms training from scratch for lightweight 4-to-6 channel configurations. DOI: [10.48550/arXiv.2602.06460](https://doi.org/10.48550/arXiv.2602.06460)

### 8\. Foundation Models | Stanford HAI

This source discusses the broader context of foundation models and their application to complex tasks like silent speech recognition. It notes that integrating LLMs as post-processing layers allows SSIs to benefit from universal language representations learned from massive text datasets. URL: [https://hai.stanford.edu/topics/foundation-models](https://hai.stanford.edu/topics/foundation-models)

### 9\. LLM-Enhanced Cross-Modal Silent Speech Recognition

This summary emphasizes how cross-modal alignment permits pretraining with audio-only datasets like LibriSpeech to improve performance on silent EMG, where data is typically scarce. It highlights the achievement of reducing word error rates below the 15% threshold, signaling the viability of SSIs for open-vocabulary human-computer interaction. URL:[https://www.emergentmind.com/papers/2403.05583](https://www.emergentmind.com/papers/2403.05583)

### 10\. Multi-modal Speech Enhancement with Limited Electromyography Channels

This study proposes a novel two-stage enhancement strategy using 8-channel EMG combined with noisy acoustic speech via a modified SEMamba network. The system significantly improves speech clarity in extremely low signal-to-noise ratio environments, achieving a PESQ gain of 0.527 under mismatched noise conditions. URL:[https://arxiv.org/abs/2501.06530](https://arxiv.org/abs/2501.06530)

### 11\. Recognition of isolated words using different sEMG-based features

This publication analyzes the efficacy of various feature extraction methods (temporal and spectral) for isolated word recognition. It provides a foundational comparison of how combinations of different sEMG-based features impact the final word error rate in early silent speech systems. URL: [https://www.researchgate.net/figure/Recognition-of-isolated-words-using-different-sEMG-based-features-Each-x-represents\_fig2\_325511974](https://www.researchgate.net/figure/Recognition-of-isolated-words-using-different-sEMG-based-features-Each-x-represents_fig2_325511974)

### 12\. Sentence-Level Silent Speech Recognition Using a Wearable EMG/EEG Sensor System with AI-Driven Sensor Fusion and Language Model

This study presents a wearable system that fuses single-channel EMG (chin) and single-channel EEG (ear) for sentence-level recognition. By utilizing a Siamese Neural Network and a trigram language model, researchers achieved 95.25% accuracy on continuous military command sentences without requiring manual word segmentation. DOI:[10.3390/s25196168](https://doi.org/10.3390/s25196168)

### 13\. Silent Speech Interfaces: Biosignal Decoding

This overview explores the diverse sensor modalities used for SSIs, including ultrasound imaging, lip video, accelerometers, and Wi-Fi backscatter. It notes that surface EMG remains the preferred approach for muscle-based SSIs due to its non-invasive nature and the fact that muscle signals lead articulatory motion by approximately 60 ms.URL: [https://www.emergentmind.com/topics/silent-speech-interfaces](https://www.emergentmind.com/topics/silent-speech-interfaces)

### 14\. Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm

This paper introduces a novel SSI approach using six-axis accelerometers to capture kinematic facial motion, decoded via a Conformer-CTC model. The system achieves 97.17% accuracy in continuous sentence recognition across English and Chinese phrases, demonstrating the potential of low-frequency motion sensors as a discrete SSI alternative. DOI:[10.48550/arXiv.2502.17829](https://doi.org/10.48550/arXiv.2502.17829)

### 15\. SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition

This research introduces SilentWear, a textile-based neckband utilizing SpeechNet (a lightweight 15k-parameter CNN) for on-device inference. The system achieves 77.5% accuracy for silent speech and demonstrates 27 hours of battery life by performing real-time decoding on a multi-core microcontroller unit (GAP9). URL:[https://arxiv.org/abs/2603.02847](https://arxiv.org/abs/2603.02847)

### 16\. Speech synthesis generalization across silent-speech interfaces

This data visualization compares the generalization of speech synthesis across different neural and neuromuscular interfaces, including ECoG, MEA, and surface EMG. It evaluates the performance of streaming RNN-T models and CTC-based decoders in reconstructing speech from varied biological inputs. URL:[https://www.researchgate.net/figure/Speech-synthesis-generalization-across-silent-speech-interfaces-a-ECoG-speech-synthesis\_fig4\_390354721](https://www.researchgate.net/figure/Speech-synthesis-generalization-across-silent-speech-interfaces-a-ECoG-speech-synthesis_fig4_390354721)

### 17\. Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones

This paper presents a discrete SSI that integrates four graphene/PEDOT:PSS-coated textile electrodes into headphone earmuffs. Using a 1D SE-ResNet architecture with squeeze-and-excitation blocks, the system adaptively weights well-coupled channels to achieve 96% accuracy on 10 control words while minimizing the impact of motion artifacts. URL:[https://arxiv.org/abs/2504.13921](https://arxiv.org/abs/2504.13921)

### 18\. emg2speech: synthesizing speech from electromyography using self-supervised speech models

This study demonstrates a strong linear relationship ($r=0.85$) between the electrical power of muscle action potentials and self-supervised speech features like those from HuBERT. By mapping EMG signals directly to these representations, the authors enable end-to-end speech generation without explicit vocoder training or articulatory models. URL: [https://arxiv.org/abs/2510.23969](https://arxiv.org/abs/2510.23969)

### 19\. emg2speech: synthesizing speech from electromyography using self-supervised speech models (Full PDF)

This full technical report details the electrode placement at 31 sites on the face and neck using SuperVisc high-viscosity gel for stable recording. It validates that even low-dimensional EMG power (31 dimensions) provides sufficient articulatory structure to naturally form distinct clusters for different articulatory gestures. URL:[https://arxiv.org/pdf/2510.23969](https://arxiv.org/pdf/2510.23969)

### 20\. EMG-to-Speech: Direct Generation of Speech From Facial Electromyographic Signals

This research provides a state-of-the-art overview of direct EMG-to-speech transformation using DNNs, LSTMs, and GMMs. It establishes a label-free approach that retains paralinguistic cues such as speaker identity and mood, proving that Feedforward DNNs are the most efficient for real-time applications. DOI: [10.1109/TASLP.2017.2738568](https://doi.org/10.1109/TASLP.2017.2738568)

### 21\. Decoding silent speech: a machine learning perspective on data, methods, and frameworks

This meta-analysis traces the evolution of SSR from early waveform analysis to current deep learning frameworks. It identifies critical requirements for efficient systems, such as noise robustness, real-time processing, and the integration of multimodal information (visual, EMG, neuroimaging) to overcome cross-subject variability. DOI: [10.1007/s00521-024-10456-z](https://doi.org/10.1007/s00521-024-10456-z)

### 22\. Modeling coarticulation in EMG-based continuous speech recognition

This paper introduces the Phonetic Feature Bundling approach to model coarticulation in EMG signals. By capturing the interdependence of phonetic features (e.g., "voiced fricative") through data-driven decision trees, the authors reduced word error rates by 33% relative, making continuous EMG speech recognition practically useful. DOI:[10.1016/j.specom.2009.12.002](https://doi.org/10.1016/j.specom.2009.12.002)

