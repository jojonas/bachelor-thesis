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



Further Ideas
=============
* Problem: better estimator for Data=1, MC<<1 (almost 0)
* Idea: Poisson->Gaussian approximation:
	* use Poisson distribution with mean mu=MC to determine probability of finding Data=0 : p(Data=0) = 0^MC/0! * exp(-MC) = exp(-MC)
	* calculate p(Data>0) = 1 - p(Data=0) = 1 - exp(-MC)
	* use this probabilty and the error/quantile function to obtain a Gaussian z (number of sigmas)
		* important: Quantile function Phi(z) = 1/2 * (1+erf(z/sqrt(2))), converts z to 1-p
		* inverse quantile function: z = Phi_inv(1-p)
		* plug in p = 1 - exp(-MC) from earlier: z = Phi_inv(1-p) = Phi_inv(exp(-MC))
	* calculate Chi' containing systematics only: Chi' = abs(MC-Data)/sigma_MC
	* both z and Chi' now represent deviations in units of sigma
	* combine z and Chi' using Gaussian error propagation: 1/Chi^2 = 1/z^2 + 1/Chi'^2 
	* Final Chi: Chi = 1/sqrt( 1/z^2 + 1/Chi'^2)
* we have to investigate the limit for Data>1, approximation p(Data>0) invalid there
* ideally should "automagically" go to Chi = abs(MC-Data)/sqrt(sigma_MC^2 + sqrt(MC)^2) = abs(MC-Data)/sqrt(sigma_MC^2 + MC)
* note: Phi, Phiinv, Erf, Erfinv should be implemented in BOOST, usually approximated by rationals

		