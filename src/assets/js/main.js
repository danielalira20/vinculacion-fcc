import { initializeNavigation } from './navigation.js';
import { initializeCatalog } from './catalog.js';
import { initializeSearch } from './search.js';
import { initializeMotion } from './motion.js';
import { initializeProcesses } from './process.js';
import { initializeAcademyVideos } from './academy-video.js';

import { initializeLearning } from './learning.js';
import { initializeCommunity } from './community.js';
import { initializeEmail } from './email.js';

initializeNavigation();
initializeCatalog();
initializeSearch();
initializeMotion();
initializeProcesses();
initializeAcademyVideos();

initializeLearning();
initializeCommunity();
initializeEmail();

import { initializePartners } from './partners.js';
initializePartners();

import { initializePromoDialog } from './promo-dialog.js';
initializePromoDialog();
