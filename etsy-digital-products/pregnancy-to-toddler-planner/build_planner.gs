/**
 * Bump to Toddler Planner — Google Sheets generator
 *
 * HOW TO USE (seller / one-time setup):
 * 1. Go to sheets.google.com > Blank spreadsheet.
 * 2. Extensions > Apps Script.
 * 3. Delete any starter code, paste this whole file in, save.
 * 4. In the function dropdown (top toolbar) pick "buildPregnancyToToddlerPlanner" and click Run.
 * 5. Authorize the script when prompted (it only edits this one spreadsheet).
 * 6. Wait ~20-30 seconds. Your finished planner will be built tab by tab.
 * 7. Rename the spreadsheet, set sharing to "Anyone with link – Viewer",
 *    and use File > Make a copy as the link you deliver to Etsy buyers
 *    (buyers should get a "make your own copy" link, not edit access to your master).
 */

// ---------- Palette ----------
var PASTEL = {
  pink: '#FBD8E5', pinkDark: '#F4AFC9',
  blue: '#D6E8F7', blueDark: '#AFD3EF',
  mint: '#D9F2E6', mintDark: '#AEE4C9',
  lavender: '#E6DFF7', lavenderDark: '#C9B8ED',
  yellow: '#FFF3CE', yellowDark: '#FBE192',
  peach: '#FDE3D3', peachDark: '#F8C39E',
  gray: '#F4F4F4', textDark: '#4A4A4A', white: '#FFFFFF',
  warnBg: '#F9D6D6', warnText: '#B33A3A',
  okBg: '#DFF3E3', okText: '#2F7A4D'
};

function onOpen() {
  SpreadsheetApp.getUi().createMenu('📋 Planner Builder')
    .addItem('Build / Rebuild Full Planner', 'buildPregnancyToToddlerPlanner')
    .addToUi();
}

function buildPregnancyToToddlerPlanner() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  ss.rename('Bump to Toddler Planner — Pregnancy to Age 2');

  // wipe existing sheets except a temp placeholder so we always have >=1 sheet
  var placeholder = ss.insertSheet('__tmp__');
  ss.getSheets().forEach(function (sh) {
    if (sh.getName() !== '__tmp__') ss.deleteSheet(sh);
  });

  buildWelcomeSheet(ss);
  buildPregnancyChecklist(ss);
  buildPrenatalTracker(ss);
  buildHospitalBagChecklist(ss);
  buildPostpartumTracker(ss);
  buildNewbornDailyLog(ss);
  buildBabyWeeklyLog(ss);
  buildGrowthTracker(ss);
  buildMilestonesChecklist(ss);
  buildVaccinationTracker(ss);
  buildDashboard(ss);

  ss.deleteSheet(placeholder);
  ss.setActiveSheet(ss.getSheetByName('Welcome'));
  SpreadsheetApp.flush();
}

// ---------- shared helpers ----------

function bannerRows(sheet, numCols, title, subtitle, bg) {
  sheet.getRange(1, 1, 1, numCols).merge().setValue(title)
    .setBackground(bg).setFontSize(18).setFontWeight('bold')
    .setFontColor(PASTEL.textDark).setHorizontalAlignment('center')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(1, 48);
  if (subtitle) {
    sheet.getRange(2, 1, 1, numCols).merge().setValue(subtitle)
      .setBackground(bg).setFontStyle('italic').setFontColor(PASTEL.textDark)
      .setHorizontalAlignment('center');
    sheet.setRowHeight(2, 26);
  }
}

function styleHeaderRow(sheet, row, headers, bg) {
  var rng = sheet.getRange(row, 1, 1, headers.length);
  rng.setValues([headers]);
  rng.setBackground(bg).setFontWeight('bold').setFontColor(PASTEL.textDark)
    .setHorizontalAlignment('center').setWrap(true);
  sheet.setFrozenRows(row);
}

function dropdown(range, options) {
  var rule = SpreadsheetApp.newDataValidation().requireValueInList(options, true).build();
  range.setDataValidation(rule);
}

function footerNote(sheet, row, numCols, text) {
  sheet.getRange(row, 1, 1, numCols).merge().setValue(text)
    .setFontStyle('italic').setFontColor(PASTEL.textDark).setWrap(true)
    .setVerticalAlignment('middle');
  sheet.setRowHeight(row, 40);
}

// A simple checklist table: [Item / Task | Done | Notes] grouped into colored sections.
function buildChecklistSheet(ss, name, tabColor, bannerColor, title, subtitle, sections, note) {
  var sheet = ss.insertSheet(name);
  sheet.setTabColor(tabColor);
  bannerRows(sheet, 3, title, subtitle, bannerColor);
  var headerRow = 3;
  styleHeaderRow(sheet, headerRow, ['Item / Task', 'Done', 'Notes'], PASTEL.gray);
  var r = headerRow + 1;
  sections.forEach(function (sec) {
    sheet.getRange(r, 1, 1, 3).merge().setValue(sec.label)
      .setBackground(sec.color || bannerColor).setFontWeight('bold').setFontColor(PASTEL.textDark);
    r++;
    var start = r;
    var values = sec.items.map(function (it) { return [it, false, '']; });
    sheet.getRange(start, 1, values.length, 3).setValues(values);
    sheet.getRange(start, 2, values.length, 1).insertCheckboxes();
    r += values.length;
  });
  if (note) footerNote(sheet, r + 1, 3, note);
  sheet.setColumnWidth(1, 340);
  sheet.setColumnWidth(2, 60);
  sheet.setColumnWidth(3, 280);
  return sheet;
}

// ---------- 1. Welcome ----------
function buildWelcomeSheet(ss) {
  var sheet = ss.insertSheet('Welcome', 0);
  sheet.setTabColor(PASTEL.lavenderDark);
  bannerRows(sheet, 3, '🤱 Bump to Toddler Planner', 'Your complete pregnancy-to-age-2 care companion', PASTEL.lavender);

  var rows = [
    ['', '', ''],
    ['How to use each tab', '', ''],
    ['Pregnancy Prep Checklist', 'Trimester-by-trimester to-dos, from first appointment to hospital pre-registration.', ''],
    ['Prenatal Health & Nutrition Tracker', 'Log weekly weight, blood pressure, vitamins and symptoms. Enter your due date once — dates fill in automatically.', ''],
    ['Hospital Bag Checklist', 'Everything to pack for mom, baby, and your support person.', ''],
    ['Postpartum Mom Recovery Tracker', 'Daily recovery log for the first 6 weeks after birth.', ''],
    ['Newborn Daily Care Log (0-3mo)', 'Feeding, diaper, sleep and temperature tracking for the newborn stage.', ''],
    ['Baby Weekly Log (3-24mo)', 'A lighter-touch weekly log once routines settle in.', ''],
    ['Baby Growth Tracker', 'Weight / height / head circumference at each well-check visit, plotted automatically.', ''],
    ['Developmental Milestones', 'General milestone reference by age band, 0-24 months.', ''],
    ['Vaccination Schedule', 'A general reference checklist — always confirm the real schedule with your pediatrician.', ''],
    ['Dashboard', 'A one-page snapshot of the charts above.', ''],
    ['', '', ''],
    ['Getting started', '', ''],
    ['1. Go to the Prenatal Health tab and enter your due date at the top.', '', ''],
    ['2. Go to the Newborn Daily Log / Baby Weekly Log tabs and enter baby’s birth date at the top once baby arrives.', '', ''],
    ['3. Check off items as you go — checkboxes and dropdowns are already built in.', '', ''],
    ['4. Duplicate the Newborn Daily Log or Baby Weekly Log sheet (right-click tab > Duplicate) if you need more rows.', '', '']
  ];
  sheet.getRange(3, 1, rows.length, 3).setValues(rows);
  sheet.getRange(4, 1).setFontWeight('bold').setFontSize(13);
  sheet.getRange(16, 1).setFontWeight('bold').setFontSize(13);
  for (var i = 5; i <= 12; i++) {
    sheet.getRange(i, 1).setFontWeight('bold');
  }

  sheet.getRange(21, 1, 1, 3).merge()
    .setValue('💡 This planner is for organizational purposes only and does not replace professional medical advice. ' +
      'Always consult your OB/GYN or pediatrician for anything health-related.')
    .setBackground(PASTEL.yellow).setFontStyle('italic').setWrap(true).setVerticalAlignment('middle');
  sheet.setRowHeight(21, 44);

  sheet.setColumnWidth(1, 340);
  sheet.setColumnWidth(2, 460);
  sheet.setColumnWidth(3, 160);
}

// ---------- 2. Pregnancy Prep Checklist ----------
function buildPregnancyChecklist(ss) {
  var sections = [
    {
      label: 'First Trimester (Weeks 1–13)', color: PASTEL.pink, items: [
        'Confirm pregnancy & schedule first prenatal visit',
        'Choose an OB/GYN or midwife',
        'Start prenatal vitamins (folic acid, iron, DHA)',
        'Share family medical history with your provider',
        'Cut out alcohol, smoking, and unpasteurized/raw foods',
        'Track early symptoms (nausea, fatigue) in the Prenatal Tracker tab',
        'Look into maternity leave / workplace policies',
        'Tell your employer (per your comfort level & policy deadlines)'
      ]
    },
    {
      label: 'Second Trimester (Weeks 14–27)', color: PASTEL.blue, items: [
        'Schedule anatomy scan / mid-pregnancy ultrasound',
        'Complete glucose screening (gestational diabetes)',
        'Research childbirth / breastfeeding classes',
        'Start nursery planning',
        'Create a gift registry / plan a baby shower',
        'Buy maternity clothes',
        'Choose a pediatrician',
        'Consider cord blood banking (optional)',
        'Start a prenatal exercise / pelvic floor routine',
        'Draft a baby name shortlist'
      ]
    },
    {
      label: 'Third Trimester (Weeks 28–40)', color: PASTEL.mint, items: [
        'Pack hospital bag (see Hospital Bag Checklist tab)',
        'Install car seat and get it inspected',
        'Write and share your birth plan',
        'Pre-register at the hospital',
        'Finish nursery & run a crib/room safety check',
        'Wash baby clothes & linens',
        'Prep and freeze meals',
        'Arrange help for the first weeks postpartum',
        'Pack documents: ID, insurance card, birth plan copies',
        'Confirm postpartum support (doula, family, partner leave)',
        'Finalize maternity leave start date'
      ]
    }
  ];
  buildChecklistSheet(ss, 'Pregnancy Prep', PASTEL.pinkDark, PASTEL.pink,
    '🤰 Pregnancy Prep Checklist', 'Trimester by trimester', sections,
    'Tip: aim to have the hospital bag and car seat done by week 36 — babies don’t always wait for your due date.');
}

// ---------- 3. Prenatal Health & Nutrition Tracker ----------
function buildPrenatalTracker(ss) {
  var sheet = ss.insertSheet('Prenatal Health');
  sheet.setTabColor(PASTEL.mintDark);
  bannerRows(sheet, 11, '🥗 Prenatal Health & Nutrition Tracker', 'Weekly log, weeks 1–40', PASTEL.mint);

  sheet.getRange(3, 1).setValue('Due date:').setFontWeight('bold');
  sheet.getRange(3, 2).setValue(new Date()).setNumberFormat('yyyy-mm-dd').setBackground(PASTEL.yellow);
  sheet.getRange(3, 3, 1, 9).merge().setValue('⬅ Enter your due date once — the Date column below fills in automatically.')
    .setFontStyle('italic');

  var headers = ['Week', 'Date', 'Weight', 'Blood Pressure', 'Swelling', 'Felt Baby Move', 'Prenatal Vitamin', 'Water (cups)', 'Iron-Rich Food', 'Calcium-Rich Food', 'Symptoms / Notes'];
  var headerRow = 4;
  styleHeaderRow(sheet, headerRow, headers, PASTEL.gray);

  var firstDataRow = headerRow + 1;
  var n = 40;
  var values = [];
  for (var w = 1; w <= n; w++) {
    values.push([w, '=$B$3-((40-' + w + ')*7)', '', '', '', '', false, '', false, false, '']);
  }
  sheet.getRange(firstDataRow, 1, n, headers.length).setValues(values);
  sheet.getRange(firstDataRow, 2, n, 1).setNumberFormat('yyyy-mm-dd');
  dropdown(sheet.getRange(firstDataRow, 5, n, 1), ['Y', 'N']);
  dropdown(sheet.getRange(firstDataRow, 6, n, 1), ['Y', 'N']);
  sheet.getRange(firstDataRow, 7, n, 1).insertCheckboxes();
  sheet.getRange(firstDataRow, 9, n, 1).insertCheckboxes();
  sheet.getRange(firstDataRow, 10, n, 1).insertCheckboxes();

  sheet.setColumnWidths(1, headers.length, 110);
  sheet.setColumnWidth(1, 55);
  sheet.setColumnWidth(11, 260);

  footerNote(sheet, firstDataRow + n + 1, headers.length,
    '⚠️ Call your provider right away for: heavy bleeding, severe headache, sudden swelling, reduced fetal movement, or fever.');
}

// ---------- 4. Hospital Bag Checklist ----------
function buildHospitalBagChecklist(ss) {
  var sections = [
    {
      label: 'For Mom', color: PASTEL.pink, items: [
        'Comfortable going-home outfit', 'Nursing bra & nursing pads', 'Maternity/postpartum pads',
        'Toiletries & travel-size essentials', 'Phone charger (long cord)', 'Slippers & robe',
        'Snacks & drinks', 'Nipple cream', 'Going-home outfit (loose, comfy)'
      ]
    },
    {
      label: 'For Baby', color: PASTEL.blue, items: [
        'Going-home outfits (2 sizes, newborn + 0-3mo)', 'Swaddle blankets', 'Newborn diapers',
        'Car seat installed & inspected', 'Hat & mittens', 'Burp cloths'
      ]
    },
    {
      label: 'For Partner / Support Person', color: PASTEL.mint, items: [
        'Change of clothes', 'Snacks', 'Entertainment (book, headphones)', 'Camera / charger', 'Pillow'
      ]
    },
    {
      label: 'Documents & Extras', color: PASTEL.yellow, items: [
        'Photo ID', 'Insurance card', 'Hospital pre-registration forms', 'Printed birth plan copies',
        'Pediatrician contact info', 'Car seat manual (for hospital staff check)'
      ]
    }
  ];
  buildChecklistSheet(ss, 'Hospital Bag', PASTEL.blueDark, PASTEL.blue,
    '🎒 Hospital Bag & Newborn Essentials', 'Pack by week 36', sections,
    'Tip: keep this bag by the door from week 36 on — check it off as you pack, not as you leave.');
}

// ---------- 5. Postpartum Mom Recovery Tracker ----------
function buildPostpartumTracker(ss) {
  var sheet = ss.insertSheet('Postpartum Mom');
  sheet.setTabColor(PASTEL.pinkDark);
  bannerRows(sheet, 10, '💗 Postpartum Mom Recovery Tracker', 'Daily log, first 6 weeks', PASTEL.pink);

  sheet.getRange(3, 1).setValue('Birth date:').setFontWeight('bold');
  sheet.getRange(3, 2).setValue(new Date()).setNumberFormat('yyyy-mm-dd').setBackground(PASTEL.yellow);
  sheet.getRange(3, 3, 1, 8).merge().setValue('⬅ Enter baby’s birth date once — dates below fill in automatically.').setFontStyle('italic');

  var headers = ['Day', 'Date', 'Bleeding / Lochia', 'Pain Level (1-5)', 'Temperature (°F)', 'Mood', 'Sleep (hrs)', 'Feeding Method', 'Rest Taken', 'Notes'];
  var headerRow = 4;
  styleHeaderRow(sheet, headerRow, headers, PASTEL.gray);
  var firstDataRow = headerRow + 1;
  var n = 42;
  var values = [];
  for (var d = 1; d <= n; d++) {
    values.push([d, '=$B$3+(' + d + '-1)', '', '', '', '', '', '', false, '']);
  }
  sheet.getRange(firstDataRow, 1, n, headers.length).setValues(values);
  sheet.getRange(firstDataRow, 2, n, 1).setNumberFormat('yyyy-mm-dd');
  dropdown(sheet.getRange(firstDataRow, 3, n, 1), ['Heavy', 'Moderate', 'Light', 'Spotting', 'None']);
  dropdown(sheet.getRange(firstDataRow, 4, n, 1), ['1', '2', '3', '4', '5']);
  dropdown(sheet.getRange(firstDataRow, 6, n, 1), ['Great', 'OK', 'Low', 'Struggling']);
  dropdown(sheet.getRange(firstDataRow, 8, n, 1), ['Breastfeeding', 'Bottle', 'Mixed']);
  sheet.getRange(firstDataRow, 9, n, 1).insertCheckboxes();

  var tempRange = sheet.getRange(firstDataRow, 5, n, 1);
  var moodRange = sheet.getRange(firstDataRow, 6, n, 1);
  var rules = sheet.getConditionalFormatRules();
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenNumberGreaterThanOrEqualTo(100.4).setBackground(PASTEL.warnBg).setFontColor(PASTEL.warnText)
    .setRanges([tempRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo('Struggling').setBackground(PASTEL.warnBg).setFontColor(PASTEL.warnText)
    .setRanges([moodRange]).build());
  sheet.setConditionalFormatRules(rules);

  sheet.setColumnWidths(1, headers.length, 105);
  sheet.setColumnWidth(1, 50);
  sheet.setColumnWidth(10, 240);

  footerNote(sheet, firstDataRow + n + 1, headers.length,
    '⚠️ Contact your provider right away for: fever ≥100.4°F, heavy bleeding (soaking a pad in under an hour), severe pain, or persistent low mood — you deserve support, not just survival.');
}

// ---------- 6. Newborn Daily Care Log (0-3mo) ----------
function buildNewbornDailyLog(ss) {
  var sheet = ss.insertSheet('Newborn Daily Log');
  sheet.setTabColor(PASTEL.blueDark);
  bannerRows(sheet, 10, '🍼 Newborn Daily Care Log', 'Birth to ~3 months — one row per day', PASTEL.blue);

  sheet.getRange(3, 1).setValue('Baby’s birth date:').setFontWeight('bold');
  sheet.getRange(3, 2).setValue(new Date()).setNumberFormat('yyyy-mm-dd').setBackground(PASTEL.yellow);
  sheet.getRange(3, 3, 1, 7).merge().setValue('⬅ Enter once — dates below fill in automatically. Duplicate this tab for month 2 / month 3.').setFontStyle('italic');

  var headers = ['Day', 'Date', 'Feedings (#)', 'Feeding Method', 'Wet Diapers (#)', 'Dirty Diapers (#)', 'Stool Color', 'Sleep (hrs)', 'Temp (°F)', 'Notes'];
  var headerRow = 4;
  styleHeaderRow(sheet, headerRow, headers, PASTEL.gray);
  var firstDataRow = headerRow + 1;
  var n = 30;
  var values = [];
  for (var d = 1; d <= n; d++) {
    values.push([d, '=$B$3+(' + d + '-1)', '', '', '', '', '', '', '', '']);
  }
  sheet.getRange(firstDataRow, 1, n, headers.length).setValues(values);
  sheet.getRange(firstDataRow, 2, n, 1).setNumberFormat('yyyy-mm-dd');
  dropdown(sheet.getRange(firstDataRow, 4, n, 1), ['Breast', 'Bottle', 'Both']);
  dropdown(sheet.getRange(firstDataRow, 7, n, 1), ['Yellow/Seedy', 'Green', 'Brown', 'Black (first days)', 'Red-streaked', 'N/A']);

  var wetRange = sheet.getRange(firstDataRow, 5, n, 1);
  var tempRange = sheet.getRange(firstDataRow, 9, n, 1);
  var stoolRange = sheet.getRange(firstDataRow, 7, n, 1);
  var rules = sheet.getConditionalFormatRules();
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenNumberLessThan(6).setBackground(PASTEL.peachDark).setFontColor(PASTEL.warnText)
    .setRanges([wetRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenNumberGreaterThanOrEqualTo(100.4).setBackground(PASTEL.warnBg).setFontColor(PASTEL.warnText)
    .setRanges([tempRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo('Red-streaked').setBackground(PASTEL.warnBg).setFontColor(PASTEL.warnText)
    .setRanges([stoolRange]).build());
  sheet.setConditionalFormatRules(rules);

  sheet.setColumnWidths(1, headers.length, 100);
  sheet.setColumnWidth(1, 45);
  sheet.setColumnWidth(10, 220);

  footerNote(sheet, firstDataRow + n + 1, headers.length,
    '⚠️ Call your pediatrician for: fewer than 6 wet diapers/day after day 5, fever ≥100.4°F (call immediately for a baby under 3 months), or black/red stool after the first days.\nRight-click this tab > Duplicate to log additional months.');
}

// ---------- 7. Baby Weekly Log (3-24mo) ----------
function buildBabyWeeklyLog(ss) {
  var sheet = ss.insertSheet('Baby Weekly Log');
  sheet.setTabColor(PASTEL.mintDark);
  bannerRows(sheet, 9, '📅 Baby Weekly Log', '3–24 months — a lighter check-in once routines settle', PASTEL.mint);

  sheet.getRange(3, 1).setValue('Baby’s birth date:').setFontWeight('bold');
  sheet.getRange(3, 2).setValue(new Date()).setNumberFormat('yyyy-mm-dd').setBackground(PASTEL.yellow);
  sheet.getRange(3, 3, 1, 6).merge().setValue('⬅ Same birth date as the Newborn Daily Log tab.').setFontStyle('italic');

  var headers = ['Week #', 'Age (months)', 'Week Of', 'Avg Feedings/Day', 'Avg Sleep (hrs/day)', 'Diapers/Day (approx)', 'Naps/Day', 'New This Week', 'Notes'];
  var headerRow = 4;
  styleHeaderRow(sheet, headerRow, headers, PASTEL.gray);
  var firstDataRow = headerRow + 1;
  var startWeek = 13, endWeek = 103;
  var n = endWeek - startWeek + 1;
  var values = [];
  for (var i = 0; i < n; i++) {
    var wk = startWeek + i;
    values.push([wk, '=ROUND(' + wk + '/4.345,1)', '=$B$3+((' + wk + '-1)*7)', '', '', '', '', '', '']);
  }
  sheet.getRange(firstDataRow, 1, n, headers.length).setValues(values);
  sheet.getRange(firstDataRow, 3, n, 1).setNumberFormat('yyyy-mm-dd');

  sheet.setColumnWidths(1, headers.length, 105);
  sheet.setColumnWidth(1, 65);
  sheet.setColumnWidth(9, 220);

  footerNote(sheet, firstDataRow + n + 1, headers.length,
    'Tip: fill this in weekly instead of daily once feeding and sleep settle into a routine, usually around 3 months.');
}

// ---------- 8. Baby Growth Tracker ----------
function buildGrowthTracker(ss) {
  var sheet = ss.insertSheet('Growth Tracker');
  sheet.setTabColor(PASTEL.lavenderDark);
  bannerRows(sheet, 6, '📏 Baby Growth Tracker', 'Weight, height & head circumference at each well-check', PASTEL.lavender);

  var headers = ['Check-up', 'Age', 'Date', 'Weight', 'Height / Length', 'Head Circumference'];
  var headerRow = 3;
  styleHeaderRow(sheet, headerRow, headers, PASTEL.gray);
  var checkups = ['Birth', '2 Weeks', '1 Month', '2 Months', '4 Months', '6 Months', '9 Months', '12 Months', '15 Months', '18 Months', '21 Months', '24 Months'];
  var firstDataRow = headerRow + 1;
  var values = checkups.map(function (c) { return [c, c, '', '', '', '']; });
  sheet.getRange(firstDataRow, 1, values.length, headers.length).setValues(values);
  sheet.setColumnWidths(1, headers.length, 140);

  // growth chart
  var labelRange = sheet.getRange(firstDataRow, 1, checkups.length, 1);
  var weightRange = sheet.getRange(firstDataRow, 4, checkups.length, 1);
  var heightRange = sheet.getRange(firstDataRow, 5, checkups.length, 1);
  var chart = sheet.newChart()
    .asType(Charts.ChartType.LINE)
    .addRange(labelRange).addRange(weightRange).addRange(heightRange)
    .setOption('title', 'Growth Curve — Weight & Height')
    .setOption('backgroundColor', PASTEL.lavender)
    .setOption('colors', [PASTEL.pinkDark, PASTEL.blueDark])
    .setOption('legend', { position: 'top' })
    .setPosition(headerRow + checkups.length + 3, 1, 0, 0)
    .build();
  sheet.insertChart(chart);

  footerNote(sheet, headerRow + checkups.length + 24, headers.length,
    'Enter the numbers from your pediatrician visits here — the chart above updates automatically.');
}

// ---------- 9. Developmental Milestones ----------
function buildMilestonesChecklist(ss) {
  var sheet = ss.insertSheet('Milestones');
  sheet.setTabColor(PASTEL.yellowDark);
  bannerRows(sheet, 4, '🧠 Developmental Milestones', 'General reference, 0–24 months', PASTEL.yellow);
  var headerRow = 3;
  styleHeaderRow(sheet, headerRow, ['Milestone', 'Achieved', 'Date Achieved', 'Notes'], PASTEL.gray);

  var bands = [
    {
      label: '0–3 Months', color: PASTEL.pink, items: [
        'Lifts head briefly during tummy time', 'Follows faces/objects with eyes',
        'Smiles responsively', 'Makes cooing sounds', 'Brings hands to mouth', 'Startles at loud sounds'
      ]
    },
    {
      label: '4–6 Months', color: PASTEL.blue, items: [
        'Rolls from tummy to back', 'Holds head steady without support', 'Reaches for and grabs objects',
        'Laughs out loud', 'Begins babbling ("ba-ba", "da-da")', 'Sits with support'
      ]
    },
    {
      label: '7–9 Months', color: PASTEL.mint, items: [
        'Sits without support', 'Crawls or scoots', 'Transfers objects hand to hand',
        'Responds to own name', 'Plays peek-a-boo', 'Picks up small objects (pincer grasp)'
      ]
    },
    {
      label: '10–12 Months', color: PASTEL.lavender, items: [
        'Pulls to stand', 'Cruises along furniture', 'May take first independent steps',
        'Says 1–2 words with meaning', 'Waves "bye-bye"', 'Points at objects of interest'
      ]
    },
    {
      label: '13–18 Months', color: PASTEL.peach, items: [
        'Walks independently', 'Says several single words', 'Follows simple one-step instructions',
        'Stacks 2–3 blocks', 'Drinks from an open cup', 'Points to a body part when asked'
      ]
    },
    {
      label: '19–24 Months', color: PASTEL.pink, items: [
        'Runs', 'Kicks a ball', 'Uses 2-word phrases', 'Follows simple 2-step instructions',
        'Shows growing independence', 'Begins pretend play'
      ]
    }
  ];
  var r = headerRow + 1;
  bands.forEach(function (b) {
    sheet.getRange(r, 1, 1, 4).merge().setValue(b.label).setBackground(b.color).setFontWeight('bold').setFontColor(PASTEL.textDark);
    r++;
    var start = r;
    var values = b.items.map(function (it) { return [it, false, '', '']; });
    sheet.getRange(start, 1, values.length, 4).setValues(values);
    sheet.getRange(start, 2, values.length, 1).insertCheckboxes();
    sheet.getRange(start, 3, values.length, 1).setNumberFormat('yyyy-mm-dd');
    r += values.length;
  });
  sheet.setColumnWidth(1, 340);
  sheet.setColumnWidth(2, 70);
  sheet.setColumnWidth(3, 120);
  sheet.setColumnWidth(4, 260);

  footerNote(sheet, r + 1, 4, 'Every baby develops at their own pace. This is a general reference, not a diagnostic tool — talk to your pediatrician with any concerns.');
}

// ---------- 10. Vaccination Schedule ----------
function buildVaccinationTracker(ss) {
  var sheet = ss.insertSheet('Vaccinations');
  sheet.setTabColor(PASTEL.lavenderDark);
  bannerRows(sheet, 6, '💉 Vaccination Schedule Tracker', 'General reference — confirm with your pediatrician', PASTEL.lavender);
  var headerRow = 3;
  styleHeaderRow(sheet, headerRow, ['Vaccine', 'Recommended Age', 'Dose #', 'Given', 'Date Given', 'Notes'], PASTEL.gray);

  var rows = [
    ['Hepatitis B', 'Birth', '1', false, '', ''],
    ['Hepatitis B', '1–2 Months', '2', false, '', ''],
    ['DTaP', '2 Months', '1', false, '', ''],
    ['IPV (Polio)', '2 Months', '1', false, '', ''],
    ['Hib', '2 Months', '1', false, '', ''],
    ['PCV13 (Pneumococcal)', '2 Months', '1', false, '', ''],
    ['Rotavirus', '2 Months', '1', false, '', ''],
    ['DTaP', '4 Months', '2', false, '', ''],
    ['IPV (Polio)', '4 Months', '2', false, '', ''],
    ['Hib', '4 Months', '2', false, '', ''],
    ['PCV13 (Pneumococcal)', '4 Months', '2', false, '', ''],
    ['Rotavirus', '4 Months', '2', false, '', ''],
    ['DTaP', '6 Months', '3', false, '', ''],
    ['Hib', '6 Months', '3', false, '', ''],
    ['PCV13 (Pneumococcal)', '6 Months', '3', false, '', ''],
    ['Rotavirus', '6 Months', '3', false, '', ''],
    ['Hepatitis B', '6–18 Months', '3', false, '', ''],
    ['Influenza', '6+ Months', 'Annual', false, '', ''],
    ['MMR', '12–15 Months', '1', false, '', ''],
    ['Varicella (Chickenpox)', '12–15 Months', '1', false, '', ''],
    ['Hepatitis A', '12–23 Months', '1', false, '', ''],
    ['PCV13 (Pneumococcal)', '12–15 Months', 'Booster', false, '', ''],
    ['Hib', '12–15 Months', 'Booster', false, '', ''],
    ['DTaP', '15–18 Months', 'Booster', false, '', ''],
    ['Hepatitis A', '18–23 Months', '2', false, '', '']
  ];
  var firstDataRow = headerRow + 1;
  sheet.getRange(firstDataRow, 1, rows.length, 6).setValues(rows);
  sheet.getRange(firstDataRow, 4, rows.length, 1).insertCheckboxes();
  sheet.getRange(firstDataRow, 5, rows.length, 1).setNumberFormat('yyyy-mm-dd');
  sheet.setColumnWidths(1, 6, 130);
  sheet.setColumnWidth(1, 190);
  sheet.setColumnWidth(6, 220);

  footerNote(sheet, firstDataRow + rows.length + 1, 6,
    '⚠️ Vaccination schedules vary by country and change over time. This is a general reference only — always follow your pediatrician’s or local health authority’s official schedule.');
}

// ---------- 11. Dashboard ----------
function buildDashboard(ss) {
  var sheet = ss.insertSheet('Dashboard');
  sheet.setTabColor(PASTEL.pinkDark);
  bannerRows(sheet, 8, '📊 Dashboard', 'A one-page snapshot of your journey', PASTEL.peach);

  var prenatal = ss.getSheetByName('Prenatal Health');
  var growth = ss.getSheetByName('Growth Tracker');
  var newborn = ss.getSheetByName('Newborn Daily Log');
  var milestones = ss.getSheetByName('Milestones');

  // Weight chart from prenatal tracker
  var weekRange = prenatal.getRange(5, 1, 40, 1);
  var weightRange = prenatal.getRange(5, 3, 40, 1);
  var chart1 = sheet.newChart().asType(Charts.ChartType.LINE)
    .addRange(weekRange).addRange(weightRange)
    .setOption('title', 'Maternal Weight by Week')
    .setOption('backgroundColor', PASTEL.blue)
    .setOption('colors', [PASTEL.pinkDark])
    .setPosition(3, 1, 0, 0).build();
  sheet.insertChart(chart1);

  // Growth chart reference (reuse growth tracker data)
  var labelRange = growth.getRange(4, 1, 12, 1);
  var wRange = growth.getRange(4, 4, 12, 1);
  var hRange = growth.getRange(4, 5, 12, 1);
  var chart2 = sheet.newChart().asType(Charts.ChartType.LINE)
    .addRange(labelRange).addRange(wRange).addRange(hRange)
    .setOption('title', 'Baby Growth Curve')
    .setOption('backgroundColor', PASTEL.mint)
    .setOption('colors', [PASTEL.pinkDark, PASTEL.blueDark])
    .setPosition(3, 6, 0, 0).build();
  sheet.insertChart(chart2);

  // Newborn feedings/diapers bar chart
  var dayRange = newborn.getRange(5, 1, 30, 1);
  var feedRange = newborn.getRange(5, 3, 30, 1);
  var wetRange = newborn.getRange(5, 5, 30, 1);
  var chart3 = sheet.newChart().asType(Charts.ChartType.COLUMN)
    .addRange(dayRange).addRange(feedRange).addRange(wetRange)
    .setOption('title', 'Newborn Feedings & Wet Diapers (Month 1)')
    .setOption('backgroundColor', PASTEL.lavender)
    .setOption('colors', [PASTEL.blueDark, PASTEL.mintDark])
    .setPosition(21, 1, 0, 0).build();
  sheet.insertChart(chart3);

  // Milestone completion scorecard
  sheet.getRange(21, 6).setValue('Milestones achieved:').setFontWeight('bold');
  sheet.getRange(22, 6).setFormula('=COUNTIF(Milestones!B:B,TRUE)&" of 36 checked"')
    .setFontSize(20).setFontWeight('bold').setFontColor(PASTEL.pinkDark);

  sheet.setColumnWidths(1, 8, 110);
}
