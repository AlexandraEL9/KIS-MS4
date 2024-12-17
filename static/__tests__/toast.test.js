const { JSDOM } = require("jsdom");
const $ = require("jquery");

describe("Bootstrap toast logic", () => {
  let dom, document;

  beforeEach(() => {
    // Mock up a DOM with a toast element
    dom = new JSDOM(`
      <!DOCTYPE html>
      <html lang="en">
        <body>
          <div class="toast" style="display: none;">Test Toast</div>
        </body>
      </html>
    `);

    // Initialize jQuery with the JSDOM environment
    document = dom.window.document;
    global.$ = require("jquery")(dom.window);

    // Mock Bootstrap's toast method
    $.fn.toast = jest.fn();
  });

  it("triggers the toast display", () => {
    // Simulate the toast logic
    $('.toast').toast('show');

    // Verify that the Bootstrap toast method was called with 'show'
    expect($.fn.toast).toHaveBeenCalledWith('show');
  });
});
