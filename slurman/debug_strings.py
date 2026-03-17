### ---> FOR DEBUGGING

SQUEUE_DEBUG = """
  JOBID PA                                     NAME  USER    STATE       TIME TIME_L NODE NODELIST(REASON)
            190689 in                              interactive bob  RUNNING       9:46 6:00:00    1 lothlann
            190663 su                             triplane3_ll bob  RUNNING    2:56:36 4-00:00:00    1 himring
            190662 su                             triplane2_ll bob  RUNNING    2:56:40 4-00:00:00    1 himring
            190661 su                             triplane1_ll bob  RUNNING    2:56:46 4-00:00:00    1 himring
            190660 su                              triplane1_l bob  RUNNING    2:57:04 4-00:00:00    1 himring
            190659 su                              triplane2_l bob  RUNNING    2:57:10 4-00:00:00    1 balrog
            190658 su                              triplane3_l bob  RUNNING    2:57:28 4-00:00:00    1 balrog
            190657 su                              triplane3_m bob  RUNNING    2:57:31 4-00:00:00    1 balrog
            190656 su                              triplane2_m bob  RUNNING    2:57:36 4-00:00:00    1 balrog
            190655 su                              triplane1_m bob  RUNNING    2:57:39 4-00:00:00    1 balrog
            190654 su                              triplane1_m bob  RUNNING    2:57:43 4-00:00:00    1 angmar
            190651 su                              triplane0_m bob  RUNNING    3:03:06 4-00:00:00    1 valinor
            190650 su                             triplane0_ll bob  RUNNING    3:03:13 4-00:00:00    1 valinor
            190649 su                              triplane0_l bob  RUNNING    3:03:17 4-00:00:00    1 valinor
"""

SINFO_DEBUG = """
HOSTNAMES           GRES                                              GRES_USED                                                                       STATE
andram              gpu:a100:4,mps:a100:400                           gpu:a100:4(IDX:0-3),mps:a100:0(IDX:N/A)                                         mix
andram              gpu:a100:4,mps:a100:400                           gpu:a100:4(IDX:0-3),mps:a100:0(IDX:N/A)                                         mix
angmar              gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
angmar              gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
balar               gpu:a100:4,mps:a100:400                           gpu:a100:4(IDX:0-3),mps:a100:0(IDX:N/A)                                         mix
balar               gpu:a100:4,mps:a100:400                           gpu:a100:4(IDX:0-3),mps:a100:0(IDX:N/A)                                         mix
balrog              gpu:rtx_3090:8,mps:rtx_3090:800                   gpu:rtx_3090:7(IDX:0-3,5-7),mps:rtx_3090:0(IDX:N/A)                             mix
balrog              gpu:rtx_3090:8,mps:rtx_3090:800                   gpu:rtx_3090:7(IDX:0-3,5-7),mps:rtx_3090:0(IDX:N/A)                             mix
char                gpu:gtx_1080:4,mps:gtx_1080:800                   gpu:gtx_1080:4(IDX:0-3),mps:gtx_1080:0(IDX:N/A)                                 mix
char                gpu:gtx_1080:4,mps:gtx_1080:800                   gpu:gtx_1080:4(IDX:0-3),mps:gtx_1080:0(IDX:N/A)                                 mix
daidalos            gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
daidalos            gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
doriath             gpu:a100:4,mps:a100:400                           gpu:a100:4(IDX:0-3),mps:a100:0(IDX:N/A)                                         mix
doriath             gpu:a100:4,mps:a100:400                           gpu:a100:4(IDX:0-3),mps:a100:0(IDX:N/A)                                         mix
erebor              gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
erebor              gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
eriador             gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
eriador             gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
falas               gpu:a100:4,mps:a100:400                           gpu:a100:3(IDX:0-2),mps:a100:0(IDX:N/A)                                         mix
falas               gpu:a100:4,mps:a100:400                           gpu:a100:3(IDX:0-2),mps:a100:0(IDX:N/A)                                         mix
gimli               gpu:rtx_3090:8,mps:rtx_3090:800                   gpu:rtx_3090:8(IDX:0-7),mps:rtx_3090:0(IDX:N/A)                                 mix
gimli               gpu:rtx_3090:8,mps:rtx_3090:800                   gpu:rtx_3090:8(IDX:0-7),mps:rtx_3090:0(IDX:N/A)                                 mix
gondor              gpu:rtx_2080:9,mps:rtx_2080:900                   gpu:rtx_2080:9(IDX:0-8),mps:rtx_2080:0(IDX:N/A)                                 mix
gondor              gpu:rtx_2080:9,mps:rtx_2080:900                   gpu:rtx_2080:9(IDX:0-8),mps:rtx_2080:0(IDX:N/A)                                 mix
himring             gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
himring             gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
hithlum             gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
hithlum             gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
ikarus              gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
ikarus              gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
lothlann            gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:8(IDX:0-7),mps:rtx_2080:0(IDX:N/A)                                 mix
lothlann            gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:8(IDX:0-7),mps:rtx_2080:0(IDX:N/A)                                 mix
moria               gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:8(IDX:0-7),mps:rtx_2080:0(IDX:N/A)                                 mix
moria               gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:8(IDX:0-7),mps:rtx_2080:0(IDX:N/A)                                 mix
pegasus             gpu:gtx_1080:8,mps:gtx_1080:800                   gpu:gtx_1080:0(IDX:N/A),mps:gtx_1080:0(IDX:N/A)                                 idle
pegasus             gpu:gtx_1080:8,mps:gtx_1080:800                   gpu:gtx_1080:0(IDX:N/A),mps:gtx_1080:0(IDX:N/A)                                 idle
ramdal              gpu:a100:4,mps:a100:400                           gpu:a100:4(IDX:0-3),mps:a100:0(IDX:N/A)                                         mix
ramdal              gpu:a100:4,mps:a100:400                           gpu:a100:4(IDX:0-3),mps:a100:0(IDX:N/A)                                         mix
seti                gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:0(IDX:N/A),mps:rtx_2080:0(IDX:N/A)                                 drain
seti                gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:0(IDX:N/A),mps:rtx_2080:0(IDX:N/A)                                 drain
sorona              gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:8(IDX:0-7),mps:rtx_2080:0(IDX:N/A)                                 mix
sorona              gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:8(IDX:0-7),mps:rtx_2080:0(IDX:N/A)                                 mix
tarsonis            gpu:gtx_1080:4,mps:gtx_1080:400                   gpu:gtx_1080:0(IDX:N/A),mps:gtx_1080:0(IDX:N/A)                                 idle
tarsonis            gpu:gtx_1080:4,mps:gtx_1080:400                   gpu:gtx_1080:0(IDX:N/A),mps:gtx_1080:0(IDX:N/A)                                 idle
umoja               gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:6(IDX:0,2-4,6-7),mps:rtx_2080:0(IDX:N/A)                           mix
umoja               gpu:rtx_2080:8,mps:rtx_2080:800                   gpu:rtx_2080:6(IDX:0,2-4,6-7),mps:rtx_2080:0(IDX:N/A)                           mix
valinor             gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
valinor             gpu:rtx_a6000:8,mps:rtx_a6000:800                 gpu:rtx_a6000:8(IDX:0-7),mps:rtx_a6000:0(IDX:N/A)                               mix
"""