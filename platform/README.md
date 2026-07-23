# The Catholic Experiment — Common Platform

This directory is the controlled source for programme-wide website standards. The common platform governs shared structure and behaviour; each Experiment retains its own subject matter, sources, course sequence and learner work.

## Approved primary navigation

### Central Catholic Experiment
Home / Courses / Schedule / Materials / Certificates / Contact

### Individual Experiments
Home / Course / Schedule / Materials / Certificates / Contact

The labels, functions and order are fixed. Experiment-specific items such as Journal, Grammar, Progress, Vocabulary, Pronunciation and Videos belong within a primary page or secondary course navigation.

## Fixed app-shell standard

Every maintained public route must use:

- the approved black-bordered frame;
- a continuous 105-pixel black desktop rail;
- a 55-pixel gold cross badge marked decorative for assistive technology;
- the six-item primary menu in the approved order;
- consistent content starting position and semantic current-page treatment;
- the same six functions in a horizontal, scrollable black navigation on mobile;
- the common 900-pixel mobile breakpoint;
- visible keyboard focus and reduced-motion support.

A landing page alone is not sufficient. Course, lesson, schedule, materials, certificates, contact, journal, terminology, glossary, vocabulary, pronunciation, about and other supporting routes must all use the shared implementation.

## Common footer standard

Every site and every maintained route uses the Latin-reference three-column footer. It contains:

1. the site name and independent-learning-project disclaimer;
2. a link whose complete linked text is **Part of The Catholic Experiment**, leading to the Catholic Experiment home page;
3. the relevant School label:
   - `School: Sacred Languages` — The Latin Experiment;
   - `School: Faith` — The Faith Experiment;
   - `School: Head Room` — The Catholic Experiment;
4. the approved AI disclosure referring to Magnifica Humanae and relevant authoritative Catholic sources;
5. the Waylight Atlantic credit in its own right-hand column.

Corrections are not linked separately from the footer. They are handled through the Contact page.

## Common Contact standard

Every site uses the same Formspree contact route and fields:

- Name;
- Email;
- Category;
- Subject;
- Message.

The approved categories are Correction, Question, Broken link, Accessibility, Suggested source and Other. The Formspree message identifies the originating Experiment through hidden subject and site fields.

## Shared source implementation

The controlled implementation consists of local copies of:

- `common-platform.css`;
- `common-platform.js`.

These files are source-identical across the central Catholic Experiment, The Latin Experiment and The Faith Experiment. Site identity, School wording, central or individual navigation labels and supporting-page active states are selected from the shared script rather than maintained through separate footer or navigation fragments.

The deployment workflow injects the shared assets into every maintained HTML route and blocks deployment when the required navigation, footer, School labels, Formspree fields, accessibility behaviour or 900-pixel breakpoint is absent.

## Reference and control rule

The Latin Experiment is the reference implementation for the app-shell geometry, footer placement, supporting-page navigation, cross accessibility and mobile behaviour. Shared geometry and behaviour may be carried to another Experiment; Latin subject content, Father Most material, Alan's journal and course-specific exercises may not.

The central Catholic Experiment remains the programme-control repository. A narrow common-platform correction must not replace a complete subject page unless the whole file has first been compared and all approved subject-specific content preserved.

## Current repository family

- Central: `Wally189/The-Catholic-Experiment`
- Latin: `Wally189/the-latin-experiment`
- Faith: `Wally189/The-Faith-Experiment`

All use the `main` branch and static or low-complexity HTML, CSS and JavaScript. Each repository holds a local, recoverable copy of the common platform assets required for its own deployment.

## Change sequence

1. Read the controlling standards and current route-specific source before editing.
2. Compare the proposed common change with the Latin reference implementation.
3. Make the smallest complete correction without importing subject content between sites.
4. Apply the same shared source to all three repositories.
5. Test every maintained route on desktop, mobile and keyboard navigation.
6. Validate the footer, School label, Formspree contact route, active states, cross accessibility and central-programme link.
7. Deploy from `main`, verify the live Pages build and record the result.

## Minimum recovery procedure

1. Sign in to the GitHub account controlling `Wally189`.
2. Clone or download the relevant repository from the `main` branch.
3. Confirm `index.html`, all maintained public routes, `common-platform.css` and `common-platform.js` are present.
4. Reconnect GitHub Pages to the repository and deploy the repository root through the controlled workflow.
5. Test every primary navigation item, lesson link, Formspree route, footer link and external source link.
6. Record the restored URL, provider, date and tester in the Common Platform Implementation Appendix.
