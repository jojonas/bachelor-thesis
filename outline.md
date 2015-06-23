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

* "Quickscan"-Algorithm (ca. 5 pages)
	* criterium: sigmas
	* criterium: nested regions
	* vertical binning
	* parameters
* Metrics: runtime, delta-p-tilde

* Delta-p-tilde spread through dicing (ca. 1 page)
* Determinism (ca. 1 page)
	* Seeding TRandom
	* Race conditions -> mitigations

* Parameter optimization (ca. 2 pages)
	* some example parameter sets

* More complete run for statistics with "optimal" parameters (ca. 1 page)

* Results: runtime, delta-p-tilde (ca. 2 pages)
	* delta-p-tilde: Full Scan (excl classes) w/o VS with quickscan
* Results on incl classes: delta-p-tilde (ca. 1 page)



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
