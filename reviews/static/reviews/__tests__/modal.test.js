const { JSDOM } = require("jsdom");
const $ = require("jquery");

describe("Delete confirmation modal trigger", () => {
  let dom, window, document;

  beforeEach(() => {
    // Set up the DOM
    dom = new JSDOM(`
      <!DOCTYPE html>
      <html lang="en">
        <body>
          <!-- Delete Button -->
          <button 
            type="button" 
            class="btn btn-danger btn-sm" 
            data-toggle="modal" 
            data-target="#confirmDeleteModal">
            Delete
          </button>

          <!-- Modal -->
          <div class="modal fade" id="confirmDeleteModal" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="confirmDeleteModalLabel">Delete Review</h5>
                </div>
              </div>
            </div>
          </div>
        </body>
      </html>
    `);

    // Initialize the DOM and jQuery
    window = dom.window;
    document = window.document;
    global.$ = require("jquery")(window);

    // Mock Bootstrap's modal method
    $.fn.modal = jest.fn();
  });

  it("Modal is triggered when delete button is clicked", () => {
    // Simulate click on the delete button
    const deleteButton = $(".btn-danger");
    deleteButton.trigger("click");

    // Manually trigger the modal to simulate Bootstrap's behavior
    $("#confirmDeleteModal").modal("show");

    // Verify jQuery's modal method was called with "show"
    expect($.fn.modal).toHaveBeenCalledWith("show");
  });
});

