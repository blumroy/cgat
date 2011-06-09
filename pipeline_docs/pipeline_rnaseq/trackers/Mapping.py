import os, sys, re, types, itertools

from SphinxReport.Tracker import *
from RnaseqReport import *

class MappingSummary( RnaseqTracker, SingleTableTrackerRows ):
    table = "view_mapping"

class TophatSummary( RnaseqTracker, SingleTableTrackerRows ):
    table = "tophat_stats"

class BamSummary( RnaseqTracker, SingleTableTrackerRows ):
    table = "bam_stats"

class AlignmentSummary( RnaseqTracker, SingleTableTrackerRows ):
    table = "alignment_stats"

class MappingContext( RnaseqTracker, SingleTableTrackerRows ):
    table = "context_stats"

class FilteringSummary( RnaseqTracker, SingleTableTrackerRows ):
    table = "mapping_stats"

class MappingFlagsMismatches( RnaseqTracker, SingleTableTrackerHistogram ):
    table = "bam_stats_nm"
    column = "nm"

class MappingFlagsHits( RnaseqTracker, SingleTableTrackerHistogram ):
    table = "bam_stats_nh"
    column = "nh"

class AlignmentQualityByCycle( RnaseqTracker, SingleTableTrackerHistogram ):
    table = "alignment_stats_quality_by_cycle_metrics"
    column = "cycle"

class AlignmentQualityDistribution( RnaseqTracker, SingleTableTrackerHistogram ):
    table = "alignment_stats_quality_distribution_metrics"
    column = "quality"

##############################################################
##############################################################
##############################################################
class BamReport( RnaseqTracker ):
    tracks = [ "all" ]

    slices = ("genome", "accepted", "mismapped" )

    def __call__(self, track, slice = None ):
        edir = EXPORTDIR

        toc_text = []
        link_text = []
        
        filenames = sorted( [x.asFile() for x in TRACKS ] )
        
        for fn in filenames:
            link = "%(slice)s_%(fn)s" % locals() 
            toc_text.append( "* %(link)s_" % locals() )
            link_text.append( ".. _%(link)s: %(edir)s/bamstats/%(fn)s.%(slice)s.html" % locals() )
            
        toc_text = "\n".join(toc_text)
        link_text =  "\n".join(link_text)

        rst_text = '''
%(toc_text)s

%(link_text)s
''' % locals()

        return odict( (("text", rst_text),) )
    

##############################################################
##############################################################
##############################################################
class FastQCReport( RnaseqTracker ):
    tracks = [ "all" ]

    def __call__(self, track, slice = None ):
        edir = EXPORTDIR

        toc_text = []
        link_text = []
        
        filenames = sorted( [x.asFile() for x in TRACKS ] )
        
        for fn in filenames:
            toc_text.append( "* %(fn)s_" % locals()) 
            link_text.append( ".. _%(fn)s: %(edir)s/fastqc/%(fn)s.genome_fastqc/fastqc_report.html" % locals() )
            
        toc_text = "\n".join(toc_text)
        link_text =  "\n".join(link_text)

        rst_text = '''
%(toc_text)s

%(link_text)s
''' % locals()

        return odict( (("text", rst_text),) )
