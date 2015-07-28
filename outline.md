Bachelor Thesis
===============

goal: ~30 pages

* Physics (max 20% = 6 pages)
	* Units (and notation)
	* Standard Model
	* LHC
		* Luminosity <-> Ndata
	* CMS
		* Detector
			* Coordinate System
		* Reco
		* Trigger

* MUSiC (ca. 5 pages)
	* Motivation
	* Workflow
		* Skimming (1 sentence)
		* Classification
		* Scanning & "Scanner Integral"
			* region building
			* p value
			* p-tilde value
			
* Motivations
	* Runtime motivation
	* at the same time: physics result untouched
	
* Difficulties/Solutions
	* concept
		* estimator
		* pre-selection
		* requirements
	* MC error only => statistical term
	* Region Plot => nested regions
	* P vs Chi => magnitude binning
	* P vs Chi => separation of excesses and deficits
		
	* Conclusion/Mitigation: Quickscan-Algorithm
		* description
		
* Optimization of the algorithm
	* parameters
	* optimization goals: 
		* delta-p-tilde
			* spread through dicing
		* runtime
	* Determinism 
		* seeds
		* race conditions
	* Results Parameter optimization on training data
		* show examples
		* 2D-plots

* Results on validation sample
	* Fullscan random dicing, Fullscan fixed seed, Qs same seed

* Final conclusion





Moneyplots
==========

* Delta-p-tilde 1D histogram: deviations smaller than random deviations
* Delta-p-tilde 2D-histograms bc of parameter optimization
* p vs. chi (fixed MC and fixed data): justify deficit/excess separation, monotonity, nested regions





TWiki
=====

* Concurrency at MUSiC: MISMaster, 1 Dicer, N scanners



Tue-Presentation
================

* Quick: MUSiC, Classification (1 slide)
* Scanning: region building, p-value (1 slide)
* P-Tilde (1 slide)
* Quickscan idea: criteria, parameters (1-2 slides)
* Metrics: runtime, delta-p-tilde (1 slide)
* Status Quo: Delta-p-tilde spread through dicing, runtime (1 slide max)
* Results: runtime, delta-p-tilde (1 slide)
* Outlook: separate subset, further performance optimizations (1 slide)
